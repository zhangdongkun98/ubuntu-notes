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
sudo apt-get install --reinstall libpng16-16=1.6.34-1
sudo apt install --reinstall libjpeg-turbo8=1.5.2-0ubuntu5
sudo apt install --reinstall libjpeg-turbo8-dev
sudo apt install libjpeg8-dev

sudo apt install libtiff-dev

sudo apt-get install build-essential clang-7 lld-7 g++-7 cmake ninja-build libvulkan1 python python-pip python-dev python3.6-dev python3-pip libpng-dev libtiff5-dev libjpeg-dev tzdata sed curl unzip autoconf libtool rsync libxml2-dev &&
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
## 2. Build carla
```bash
git clone -b https://github.com/carla-simulator/carla.git
```


maybe optional:
```python
distutils.unixcompiler.UnixCCompiler:
def _compile
    if '-specs=/usr/share/dpkg/no-pie-compile.specs' in compiler_so:
        compiler_so.remove('-specs=/usr/share/dpkg/no-pie-compile.specs')
```

修改  download_content
```bash
function download_content {
  cp ~/carla_server/save/Content.tar.gz .
  mkdir -p Content
  tar -xvzf Content.tar.gz -C Content
  # rm Content.tar.gz
  mkdir -p "$CONTENT_FOLDER"
  mv Content/* "$CONTENT_FOLDER"
  rm -rf Content
  echo "$CONTENT_ID" > "$VERSION_FILE"
  echo "Content updated successfully."
}
```

```bash
echo "export UE4_ROOT=~/UnrealEngine_4.22" >> ~/.bashrc
source ~/.bashrc
```

```bash
make CarlaUE4Editor
make PythonAPI
make build.utils
make package
```


## 3. Build summit
[build](https://adacompnus.github.io/summit-docs/getting_started/building/)
```bash
sudo apt install ccache
```

```bash
cp CustomAssets/EmptyMap.umap Unreal/CarlaUE4/Content/Carla/Maps/TestMaps/EmptyMap.umap
cp CustomAssets/EmptyMap_BuiltData.uasset Unreal/CarlaUE4/Content/Carla/Maps/TestMaps/
cp CustomAssets/M_Tile.uasset Unreal/CarlaUE4/Content/Carla/Static/GenericMaterials/Ground/
```
