# (On Ubuntu 18.04)
# UE4.22, CARLA0.9.8
## 0. Requirements
```bash
conda deactivate
```

```bash
sudo apt-get update &&
sudo apt-get install wget software-properties-common &&
sudo add-apt-repository ppa:ubuntu-toolchain-r/test &&
wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|sudo apt-key add - &&
sudo apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-7 main" &&
sudo apt-get update
```

```bash
sudo apt-get install build-essential clang-7 lld-7 g++-7 cmake ninja-build libvulkan1 python python-pip python-dev python3-dev python3-pip libpng-dev libtiff5-dev libjpeg-dev tzdata sed curl unzip autoconf libtool rsync libxml2-dev &&
pip2 install --user setuptools &&
pip3 install --user setuptools 
```

```bash
sudo update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-7/bin/clang++ 170 &&
sudo update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-7/bin/clang 170
```

## 1. Build UE4
```bash
git clone --depth=1 -b 4.22 https://github.com/EpicGames/UnrealEngine.git ~/UnrealEngine_4.22

cd ~/UnrealEngine_4.22
./Setup.sh && ./GenerateProjectFiles.sh && make
cd ~/UnrealEngine_4.22/Engine/Binaries/Linux && ./UE4Editor
```
