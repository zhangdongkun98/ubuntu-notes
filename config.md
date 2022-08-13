
# 终端快捷方式
[addr](https://www.cnblogs.com/cobbliu/p/3629772.html)

# 全屏显示
[addr](https://blog.csdn.net/nuddlle/article/details/77994080)

```sh
sudo apt-get install open-vm-tools
sudo apt-get install open-vm*
reboot
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

### 修改端口

```bash
vim /etc/ssh/sshd_config
/etc/init.d/ssh restart
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

### install

```bash
sudo apt install tmux
```

### 默认配置

```bash
cd
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
```

### 修改prefix前缀快捷键

[blog](https://www.tkmiss.com/archives/105.html)

```bash
vim ~/.tmux.conf   ### or ~/.tmux.conf.local if has this file
  set -g prefix C-x
  unbind C-b
  bind C-x send-prefix
```




# Google Cloud CLI / gsutil

[web](https://cloud.google.com/storage/docs/gsutil_install#deb) <br>

```bash
sudo apt-get install apt-transport-https ca-certificates gnupg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install google-cloud-cli
gcloud init
```
