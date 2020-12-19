# clang

	sudo apt install clang-7 lld-7

- version 6.0
```
libclang-common-6.0-dev libclang1-6.0 libomp-dev libomp5 llvm-6.0 llvm-6.0-dev llvm-6.0-runtime
```
- version 7.1
```
	clang-7 libclang-common-7-dev libclang1-7 libllvm7 libomp-7-dev libomp5-7 lld-7 F llvm-7-dev llvm-7-runtime
```

- version 8.0
```
	libclang-common-8-dev libclang1-8 libllvm8 libomp-8-dev libomp5-8 llvm-8 llvm-8-dev llvm-8-runtime
```

- version 7.0 (手动安装)
[下载](https://releases.llvm.org/download.html#7.0.0)
```
cd opt/clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04
	
安装（-n可省略）：
sudo cp -r -n bin/* /usr/bin
sudo cp -r -n include/* /usr/include/
sudo cp -r -n lib/* /usr/lib
sudo cp -r -n libexec/* /usr/libexec/
sudo cp -r -n share/* /usr/share/

sudo update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-7/bin/clang++ 170 &&
sudo update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-7/bin/clang 170

卸载（见目录附件）：
cat installed.txt | xargs sudo rm -f
```