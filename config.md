# 终端快捷方式
[addr](https://www.cnblogs.com/cobbliu/p/3629772.html)

# 全屏显示
[addr](https://blog.csdn.net/nuddlle/article/details/77994080)

```sh
sudo apt-get install open-vm-tools
sudo apt-get install open-vm*
reboot
```


# 使用国内镜像服务器，解决apt-get、pip等安装工具下载依赖包速度慢的问题
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



# 科学上网
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
[dependency](https://github.com/qingshuisiyuan/electron-ssr-backup/blob/master/Ubuntu.md)

```sh
sudo apt-get -f install libappindicator1 libindicator7
见附件
```

## proxychains-ng (proxychains4)
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

[addr](https://kingfast.cc/docs/#/clash/linux)

[download](https://github.com/Dreamacro/clash/releases/)

```bash
# clash文件见附件
chmod +x clash
curl  你的clash订阅链接 > $HOME/.config/clash/config.yaml   ### ! warning: check $HOME/.config/clash/config.yaml manually
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



# Terminator
[blog](https://zhuanlan.zhihu.com/p/144711440)

	sudo apt install terminator


美化 ~/.config/terminator/config

```config
[global_config]
  inactive_color_offset = 0.71
  suppress_multiple_term_dialog = True
  title_font = Ubuntu Mono 11[keybindings]
[keybindings]
  copy = <Primary><Shift>c
  switch_to_tab_1 = <Alt>1
  switch_to_tab_2 = <Alt>2
  switch_to_tab_3 = <Alt>3
  switch_to_tab_4 = <Alt>4
  switch_to_tab_5 = <Alt>5
  switch_to_tab_6 = <Alt>6
  switch_to_tab_7 = <Alt>7
  switch_to_tab_8 = <Alt>8
  switch_to_tab_9 = <Alt>9
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
    background_darkness = 0.92
    background_image = None
    background_type = transparent
    font = Ubuntu Mono 10
    foreground_color = "#f9fbf8"
    scroll_on_output = False
    scrollback_lines = 500000
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




# MP4
```bash
sudo apt-get install ubuntu-restricted-extras
```

# FTP
[maybe useful](https://devanswers.co/installing-ftp-server-vsftpd-ubuntu-18-04/)
```bash
sudo apt install vsftpd
sudo systemctl status vsftpd
```

# 中文乱码 (18.04)
[blog](http://www.jrjxdiy.com/linux/ubuntu-18-04-the-solution-of-displaying-messy-code-in-chinese-for-txt-file.html)

```bash
dconf-editor

# 展开org/gnome/gedit/preferences/encodings/candidate-encodings
# Use Default value 关闭
# Custom value 增加['UTF-8', 'GB18030', 'GB2312', 'GBK', 'BIG5', 'CURRENT', 'UTF-16']

# 系统设置内添加中文语言
```




# tmux

```bash
sudo apt install tmux

cd
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
```

