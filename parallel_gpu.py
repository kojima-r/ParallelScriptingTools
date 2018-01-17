import gpustat
import joblib
from joblib import Parallel, delayed
import os
import multiprocessing
import sys

def info(cmd):
	worker=multiprocessing.current_process()._identity
	if len(worker)==0:
		worker_id=-1
	else:
		worker_id=worker[0]-1
		print("cmd:"+cmd)
		#print('module name:', __name__)
		#print('parent process:', os.getppid())
		#print('process id:', os.getpid())
		#print('worker id:', worker_id)
		os.environ["CUDA_VISIBLE_DEVICES"] = str(worker_id)
		#os.system("echo $CUDA_VISIBLE_DEVICES "+str(worker_id))
		os.system(cmd)

if __name__ == '__main__':
	if len(sys.argv)<2:
		print("usage python parallel_gpu.py <list>")
		quit()
	cmds=[line.strip() for line in open(sys.argv[1])]
	s = gpustat.GPUStatCollection.new_query()
	ngpu=len(s)
	assigned_gpur=[0 for _ in range(ngpu)]
	result = Parallel(n_jobs=ngpu)([delayed(info)(cmd) for cmd in cmds])

	#with Pool(processes=ngpu) as pool:
	#	for i in pool.imap_unordered(f, range(10)):
	#		print("xx",i)

	

