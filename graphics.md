

# 查看显卡型号及NVIDIA驱动版本

```sh
lspci | grep -i nvidia

sudo dpkg --list | grep nvidia-*
cat /proc/driver/nvidia/version
```

# 版本匹配
```bash
NVIDIA-Linux-x86_64-455.23.04.run
cuda_11.1.0_455.23.05_linux.run
cudnn-11.1-linux-x64-v8.0.4.30.tgz/8.0.5.39
```

# NVIDIA驱动
[安装](https://blog.csdn.net/wsp_1138886114/article/details/89406911)

```sh
sudo gedit /etc/modprobe.d/blacklist.conf
	blacklist nouveau
	options nouveau modeset=0
sudo update-initramfs -u
lsmod | grep nouveau

官网https://www.geforce.cn/drivers下载对应版本，下载至home目录下（目录自定义，但是不要有中文）（尽量新，避免循环登录问题）（见附件）
按ctrl+alt+f1进入命令行界面(ctrl+alt+f7返回桌面)，登录
sudo service lightdm stop      //这个是关闭图形界面，不执行会出错。
sudo apt-get remove nvidia-*  （若无，请跳过该命令）
sudo chmod  a+x NVIDIA-Linux-x86_64-440.64.run
sudo ./NVIDIA-Linux-x86_64-418.43.run -no-x-check -no-nouveau-check -no-opengl-files
	#只有禁用opengl这样安装才不会出现循环登陆的问题
	安装参数说明：
	-no-x-check：安装驱动时关闭X服务
	-no-nouveau-check：安装驱动时禁用nouveau
	-no-opengl-files：只安装驱动文件，不安装OpenGL文件；carla需要opengl
sudo service lightdm start             # 重启服务
modprobe nvidia    // 挂载
nvidia-smi
```

[安装](https://www.jianshu.com/p/d45434f28ca0)
	
```sh
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update

sudo apt-get remove --purge nvidia-*
sudo apt-get autoremove
sudo apt-get install -f
sudo reboot

ubuntu-drivers devices     #查看合适的显卡驱动版本
sudo apt install nvidia-430
```


# CUDA
## cuda10.1
[document](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)
[doc](https://docs.nvidia.com/cuda/archive/10.1/)
[Linux安装CUDA的正确姿势](https://blog.csdn.net/wf19930209/article/details/81879514)
[Ubuntu 16.04 安装 CUDA10.1 （解决循环登陆的问题）](https://www.cnblogs.com/dinghongkai/p/11268976.html)
[Setting up Ubuntu 16.04 + CUDA + GPU for deep learning with Python](https://www.pyimagesearch.com/2017/09/27/setting-up-ubuntu-16-04-cuda-gpu-for-deep-learning-with-python/)

```bash
# ctr + alt + F1 进入tty1，禁止X server
sudo service lightdm stop

sudo bash cuda_xxx.run
	参数如下：
	--no-opengl-libs：表示只安装驱动文件，不安装OpenGL文件。必需参数，原因同上。注意：不是-no-opengl-files。
	--uninstall (deprecated)：用于卸载CUDA Driver（已废弃）。
	--toolkit：表示只安装CUDA Toolkit，不安装Driver和Samples
	--help：查看更多高级选项
sudo apt install nvidia-cuda-toolkit
nvcc -V    # 若显示版本信息则成功
cat /usr/local/cuda/version.txt

#编译并测试设备 deviceQuery：
cd ～/NVIDIA_CUDA-10.1_Samples/1_Utilities/deviceQuery
make
./deviceQuery
#编译并测试带宽 bandwidthTest：
cd ../bandwidthTest
make
./bandwidthTest
# 若这两个测试的最后结果都是Result = PASS，说明CUDA安装成功
```

## CUDA Toolkit 11.2 Download
[doc](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal)
```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.2.0/local_installers/cuda-repo-ubuntu1804-11-2-local_11.2.0-460.27.04-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804-11-2-local_11.2.0-460.27.04-1_amd64.deb
sudo apt-key add /var/cuda-repo-ubuntu1804-11-2-local/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
```

## CUDA Toolkit 11.0 Download
[doc](https://developer.nvidia.com/cuda-11.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal)
```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda-repo-ubuntu1804-11-0-local_11.0.2-450.51.05-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804-11-0-local_11.0.2-450.51.05-1_amd64.deb
sudo apt-key add /var/cuda-repo-ubuntu1804-11-0-local/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
```

## remove cuda
[How to remove cuda completely from ubuntu?](https://stackoverflow.com/questions/56431461/how-to-remove-cuda-completely-from-ubuntu)
```bash
sudo apt-get --purge remove "*cublas*" "cuda*" "nsight*"
sudo apt-get --purge remove "*nvidia*"
sudo rm -rf /usr/local/cuda*
sudo rm /etc/apt/sources.list.d/...
sudo apt-get update

sudo apt-get purge nvidia*
sudo apt-get autoremove
sudo apt-get autoclean
sudo rm -rf /usr/local/cuda*

cd /usr/local/cuda-10.2/bin
./cuda-uninstaller
```



# cuDNN
[download](https://developer.nvidia.com/rdp/cudnn-download)

[Ubuntu16.04配置cuda+cuDNN](https://blog.csdn.net/lulugay/article/details/83316886)

```bash
sudo dpkg -i libcudnn7_7.6.5.32-1+cuda10.1_amd64.deb
sudo dpkg -i libcudnn7-dev_7.6.5.32-1+cuda10.1_amd64.deb
sudo dpkg -i libcudnn7-doc_7.6.5.32-1+cuda10.1_amd64.deb

cd /usr/src/cudnn_samples_v7/conv_sample
sudo make
./conv_sample
```
