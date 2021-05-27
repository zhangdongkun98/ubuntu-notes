
关闭secure boot

[ROG 幻14 完美安装Linux Ubuntu LTS 20.04 解决各种问题](https://leanote.zzzmh.cn/blog/post/admin/ROG-%E5%B9%BB14-%E5%AE%8C%E7%BE%8E%E5%AE%89%E8%A3%85Ubuntu-20.04)

### rog-core

```bash
sudo apt install rustc cargo make
sudo apt install libdbus-1-dev 
sudo apt install llvm
sudo apt install libclang-dev 
sudo apt-get install clang

git clone https://github.com/flukejones/rog-core.git
cd rog-core
make
sudo make install
```
