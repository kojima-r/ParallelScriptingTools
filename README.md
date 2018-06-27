# ParallelScriptingTools
並列化ツール

## 準備
一行１コマンドのコマンドリストのファイルを作成します
例
```
echo "work1"
echo "work2"
echo "work3"
...
```
## 実行

コマンドリストを上から順に並列に実行します。
一度に実行する数はCPUの場合はプロセス数を指定する必要があります。
GPUの場合は利用できるGPUの数になります。


### CPU
```
ruby parallel.py <#process> <コマンドリストファイル> [<sleep_time>]
```

オプション：sleep_timeは一つのプロセス終了後に次のプロセスを開始するまでの時間（sec）

### GPU

```
python parallel_gpu.py <コマンドリストファイル>
```
