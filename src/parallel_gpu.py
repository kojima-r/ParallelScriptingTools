import gpustat
import joblib
from joblib import Parallel, delayed
import os
import multiprocessing
import argparse
import sys
def init(queue):
    global idx
    idx = queue.get()


def info(args):
    global idx
    cmd=args
    worker=multiprocessing.current_process()._identity
    #print(idx)
    if len(worker)==0:
        worker_id=-1
    else:
        print("cmd:"+cmd," workewr=",str(idx))
        #worker_id=worker[0]-1
        #print('module name:', __name__)
        #print('parent process:', os.getppid())
        #print('process id:', os.getpid())
        #print('worker id:', worker_id)
        os.environ["CUDA_VISIBLE_DEVICES"] = str(idx)
        os.system(cmd)

 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("list", type=str, help="command list ")
    parser.add_argument(
        "--gpu_num", type=int, default=None, nargs="?", help="config json file"
    )
    parser.add_argument(
        "--save_config", type=str, default=None, nargs="?", help="config json file"
    )
    parser.add_argument("--profile", action="store_true", help="")
    args = parser.parse_args()
    #
    cmds=[line.strip() for line in open(args.list)]
    s = gpustat.GPUStatCollection.new_query()
    ngpu=len(s)

    manager = multiprocessing.Manager()
    idQueue = manager.Queue()
    for i in range(ngpu):
        idQueue.put(i)

    p = multiprocessing.Pool(ngpu, init, (idQueue,))
    result = p.map(info,[cmd for cmd in cmds])


if __name__ == '__main__':
    main()	

