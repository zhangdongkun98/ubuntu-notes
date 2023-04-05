
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


### 显卡驱动

[ROG幻14安装Ubuntu20.04及nvidia-455显卡驱动](https://zhuanlan.zhihu.com/p/386021063)
[ROG Zephyrus G14（幻14）G15 Ubuntu 20.04 双系统安装避坑指南（4800H AMD Nvidia GPU核显独显问题，快捷键Fn键盘灯驱动）](https://blog.csdn.net/qq_19951409/article/details/113805736)

装完显卡驱动后不要重启

```bash
### 进入 /usr/share/X11/xorg.conf.d/10-nvidia.conf， 添加
    Option "PrimaryGPU" "No"

update-grub
```




### 多显示器(20.04)

[Asus ROG Zephyrus G14 / 幻14 Ubuntu 外接HDMI显示屏检测不到，AMD核显驱动配置，AMD+Nvidia双显卡配置](https://blog.csdn.net/weixin_53242716/article/details/110948529)

```bash
### 1. add mdgpu.exp_hw_support=1
sudo vim /etc/default/grub
##### in file
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amdgpu.exp_hw_support=1"
##### exit file

sudo update-grub
reboot

### 2. forbid nouveau
sudo vim /etc/modprobe.d/blacklist-nouveau.conf
##### in file
blacklist nouveau
options nouveau modeset=0
##### exit file

sudo update-initramfs -u
reboot
lsmod | grep nouveau

### 3. install nvidia-driver

### 4. primary gpu
sudo vim /usr/share/X11/xorg.conf.d/10-amdgpu.conf
##### in file
Section "OutputClass"
    Identifier "AMDgpu"
    MatchDriver "amdgpu"
    Driver "amdgpu"
    Option "PrimaryGPU" "no"
EndSection
##### exit file

sudo vim /usr/share/X11/xorg.conf.d/10-nvidia.conf
##### in file
Section "OutputClass"
	Identifier "nvidia"
	MatchDriver "nvidia-drm"
	Driver "nvidia"
	Option "AllowEmptyInitialConfiguration"
	Option "PrimaryGPU" "yes"
	ModulePath "/usr/lib/x86_64-linux-gnu/nvidia/xorg"
EndSection
##### exit file


```

