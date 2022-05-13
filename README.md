# ParallelScriptingTools
GPU用並列化ツール
マシンに積んであるGPUの数だけ並列化し、適宜前のコマンドが実行され次第、次のコマンドを実行していきます。
１コマンドに１GPUを割り当てて比較的無駄なく、複数の実行コマンドを実行します。

## インストール
```
pip install git+https://github.com/kojima-r/ParallelScriptingTools.git
pip install gpustat
```

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

### GPU

```
parallel-gpu <コマンドリストファイル>
```

# linuxの場合は以下のコマンド相当
```
cat <コマンドリストファイル> | xargs -P<#process> -I{} -t bash -c '{}'
```
