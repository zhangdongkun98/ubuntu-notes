## 终端快捷方式
[addr](https://www.cnblogs.com/cobbliu/p/3629772.html)

## Ubuntu全屏显示
[addr](https://blog.csdn.net/nuddlle/article/details/77994080)

```sh
sudo apt-get install open-vm-tools
sudo apt-get install open-vm*
reboot
```


## 使用国内镜像服务器，解决apt-get、pip等安装工具下载依赖包速度慢的问题
```sh
mkdir ~/.pip		# 如果不存在此文件夹，则创建之
vim ~/.pip/pip.conf
	内容如下：
		[global]
		index-url=http://mirrors.aliyun.com/pypi/simple/
		[install]
		trusted-host=mirrors.aliyun.com
cd /etc/apt
sudo cp sources.list sources.list.bak		# 将原配置文件备份
sudo vim sources.list		# 修改配置文件
	内容如下：
	# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
	deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
	# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
	deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
	# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
	deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
	# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
	deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
	# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse

	# 预发布软件源，不建议启用
	# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
	# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
sudo apt-get update
```



# ubuntu 16.04科学上网
## SS
[安装](https://zhoukay.top/2018/09/16/Ubuntu16-04%E9%85%8D%E7%BD%AEshadowsocks-qt5%E5%AE%A2%E6%88%B7%E7%AB%AF/)

```sh
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt-get update
sudo apt-get install shadowsocks-qt5
```
## ssr
[addr1](https://mumumushi.github.io/2018/09/06/use_ssr_in_Linux/)
[addr2](https://samzong.me/2017/11/17/howto-use-ssr-on-linux-terminal/)

```sh
**安装配置ssr**
wget https://onlyless.github.io/ssr
sudo mv ssr /usr/local/bin
sudo chmod 766 /usr/local/bin/ssr
ssr install
ssr config
根据自己的购买的ssr所提供的信息填写
（设置开机自启）sudo vim /etc/rc.local
（在exit 0之前添加）sudo ssr start

**安装配置SwitchyOmega**
安装插件
	将SwitchyOmega.crx后缀改为zip并解压，然后从google导入
编辑一个情景模式，重命名为gfwlist
代理协议选择SOCKS5
代理服务器为127.0.0.1
代理端口为1080
```
## electron-ssr
[原址](https://github.com/chenchaohan/electron-ssr)
[备份](https://github.com/qingshuisiyuan/electron-ssr-backup)

```sh
sudo apt-get -f install libappindicator1 libindicator7
见附件
```

## AnyConnect  v2ray todo ....

## proxychains-ng(proxychains4)
[addr](https://www.cnblogs.com/xuyaowen/p/proxychians4.html)

```bash
git clone https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng
./configure --prefix=/usr --sysconfdir=/etc
make
sudo make install
sudo make install-config
```


## clash
[addr]https://kingfast.cc/docs/#/clash/linux

```bash
# clash文件见附件
chmod +x clash
curl  你的clash订阅链接 > $HOME/.config/clash/config.yaml
./clash
    # Can't find MMDB, start download
    https://github.com/Dreamacro/maxmind-geoip/releases/latest/download/Country.mmdb
# SwitchOmega 端口7891

# 更改proxychains配置文件
proxychains4: /usr/local/etc/proxychains.conf
unknown: /etc/proxychains.conf

# 对当前终端都使用代理
proxychains4 bash
```


# NVIDIA驱动，CUDA，cuDNN
## 查看显卡型号及NVIDIA驱动版本

```sh
lspci | grep -i nvidia

sudo dpkg --list | grep nvidia-*
cat /proc/driver/nvidia/version
```

## NVIDIA驱动
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


## cuDNN
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



# 实时网速

[addr](https://www.cnblogs.com/cyq632694540/p/11672760.html)

```sh
sudo apt-get install bmon
bmon -p eth0
```

## 命令行测网速（带宽）
[addr](https://blog.csdn.net/LeonSUST/article/details/80726402)

```sh
sudo apt install speedtest-cli
speedtest-cli
```

## 切换高性能模式

[addr](https://blog.csdn.net/zhanghm1995/article/details/86484096)

```sh
sudo apt-get install indicator-cpufreq
重启电脑
电脑右上角出现图标，可以选择节能模式还是高性能模式

# 以下命令可以查看当前电脑CPU工作模式
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

# Qt4与Qt5切换

```sh
qtcreator -version
qtchooser -list-versions
cd /usr/lib/x86_64-linux-gnu/qt-default/qtchooser
sudo gedit default.conf
```

# 安装OpenBLAS

[addr1](https://blog.csdn.net/tekkie/article/details/90903108) [addr2](https://www.cnblogs.com/chay/p/10272949.html)

```sh
https://github.com/xianyi/OpenBLAS/releases  下载你喜欢的版本解压到指定目录
cd OpenBLAS
make -j4
sudo make install #默认安装在/opt/OpenBLAS下
#也可以执行以下命令，指定安装目录
sudo make --PREFIX=/usr/local/OpenBLAS/ install #--PREFIX=表示安装目录前缀

ln -s /opt/OpenBLAS/lib/libopenblas.so.0   /usr/lib/libopenblas.so.0

gcc test.c  -I /opt/OpenBLAS/include/ -L/opt/OpenBLAS/lib -lopenblas
```

# 忽略笔记本合盖休眠
```sh
# 打开terminal：
sudo vim /etc/systemd/logind.conf
    然后将其中的：
    #HandleLidSwitch=suspend
    改成：
    HandleLidSwitch=ignore
# 然后重启服务：？
sudo restart systemd-logind
```

# 配置SSH

```sh
# 安装
sudo apt install openssh-server
# 开启
sudo service ssh start
# 查看
sudo ps -e | grep ssh
```

```sh
# 开机自动启动ssh命令
sudo systemctl enable ssh

# 关闭ssh开机自动启动命令
sudo systemctl disable ssh

# 单次开启ssh
sudo systemctl start ssh

# 单次关闭ssh
sudo systemctl stop ssh

# 设置好后重启系统
reboot

#查看ssh是否启动，看到Active: active (running)即表示成功
sudo systemctl status ssh

```



# 更新内核

[blog](https://linux.cn/article-8284-1.html) [blog](https://blog.csdn.net/weixin_40641735/article/details/89019657)
[kernel version](https://kernel.ubuntu.com/~kernel-ppa/mainline/)
[extra](https://askubuntu.com/questions/1091671/how-to-monitor-ryzen-temperatures-on-ubuntu-18-04)

```bash
### 安装libssl1.1
# 添加源
echo "deb http://security.ubuntu.com/ubuntu bionic-security main" >> /etc/apt/sources.list
sudo apt update
sudo apt install libssl1.1

### 安装新内核（5.0.0-050000rc1-generic）
# 下载地址https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.0-rc1/
sudo dpkg -i *.deb
uname -sr
```



# WINE(待测试)

https://www.jianshu.com/p/f7f0c4792c75



## Terminator
[blog](https://zhuanlan.zhihu.com/p/144711440)

	sudo apt install terminator


美化 ~/.config/terminator/config

```config
[global_config]
	suppress_multiple_term_dialog = True
	title_font = Ubuntu Mono 11[keybindings]
[keybindings]
[layouts]
	[[default]]
		[[[child1]]]
			parent = window0
			type = Terminal
		[[[window0]]]
			parent = ""
			type = Window
[plugins]
[profiles]
	[[default]]
        background_color = "#002b36"
        background_darkness = 0.91
        background_image = None
        background_type = transparent
        font = Ubuntu Mono 14
        foreground_color = "#f9fbf8"
        show_titlebar = False
        use_system_font = False
```

~/.bashrc

```bash
# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    # PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    PS1="\[\e[01;32;36m\]\u\[\e[37;33m\]@\h: \[\e[36;32m\]\w\[\e[0m\]\\$ "
    ;;
*)
    ;;
esac
```


## Docker

[blog](https://blog.csdn.net/jinking01/article/details/82490688)

```bash
sudo apt-get remove docker docker-engine docker-ce docker.io
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce
systemctl status docker
sudo systemctl start docker
sudo docker run hello-world
```



[a bug](https://www.digitalocean.com/community/questions/how-to-fix-docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket)

	sudo chmod 666 /var/run/docker.sock



## conda



```bash
sh Miniconda3-latest-Linux-x86_64.sh -b
~/miniconda3/bin/conda init
conda create --name d2l python=3.7.7 -y
```
