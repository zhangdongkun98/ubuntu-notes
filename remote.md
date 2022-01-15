# VNC

## Install and Configure


[Ubuntu18.04LTS安装TigerVNC](https://blog.csdn.net/fjmsonic/article/details/104366421)

### install

```bash
sudo apt install xfce4 xfce4-goodies xorg dbus-x11 x11-xserver-utils
sudo apt-get install gnome-session-flashback
sudo apt-get install gnome-panel
sudo apt-get install ubuntu-gnome-desktop
sudo systemctl start gdm
sudo systemctl enable gdm

sudo apt install tigervnc-standalone-server tigervnc-common
```

### ~/.vnc/xstartup

```bash
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
startxfce4 &    #启动xface4
[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
xsetroot -solid grey    #设置背景色
```

```bash
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

vncconfig -iconic &
dbus-launch --exit-with-session gnome-session &
```

### configure and use

```bash
vncpasswd
```


```bash
vncserver :1 -localhost no -geometry 2240x1260 -depth 32
vncserver -kill :1
```


## deprecated


[Ubuntu18.04 LTS 安装 VNC Server](https://blog.csdn.net/yidichaxiang/article/details/96429007)
[Ubuntu18.04 LTS 安装 VNC Server[x11vnc,tightvncserver,vnc4server]](https://blog.csdn.net/yidichaxiang/article/details/100533237#commentBox)
[Installation of VNC server on Ubuntu](https://zhuanlan.zhihu.com/p/162086445)

```bash
sudo apt install xfce4 xfce4-goodies xorg dbus-x11 x11-xserver-utils
sudo apt install tigervnc-standalone-server tigervnc-common

sudo apt install tigervnc-standalone-server tigervnc-common tigervnc-xorg-extension tigervnc-viewer

sudo apt-get install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
sudo apt-get install --no-install-recommends ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal gnome-core

netstat -anp
netstat -tulpn

```


```bash
# 从https://dl.bintray.com/tigervnc/stable/ubuntu-16.04LTS/amd64/下载
tigervncserver_1.7.0-1ubuntu1_amd64.deb
```


### ~/.vnc/xstartup
```bash
#!/bin/sh
 
# Uncomment the following two lines for normal desktop:
export XKL_XMODMAP_DISABLE=1
unset SESSION_MANAGER
# exec /etc/X11/xinit/xinitrc
unset DBUS_SESSION_BUS_ADDRESS
 
gnome-panel &
gnmoe-settings-daemon &
metacity &
nautilus &
gnome-terminal &
```

```bash
#!/bin/sh
exec /etc/vnc/xstartup
xrdb $HOME/.Xresources
vncconfig -iconic &
dbus-launch --exit-with-session gnome-session &
```

```bash
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec startxfce4
```


### TigerVNC
[install deb](http://tigervnc.bphinz.com/nightly/)
[github](https://github.com/TigerVNC/tigervnc/releases)

- For 18.04, use tigervncserver_1.11.80+20210518git2a042c91-1ubuntu1_amd64.deb
```bash
vncserver :3 -localhost no -geometry 2240x1260 -depth 32
vncserver -kill :3
```


### realvnc （图形界面）

[vnc server](https://www.realvnc.com/en/connect/download/vnc/)
[vnc viewer](https://www.realvnc.com/en/connect/download/viewer/)
[blog](https://blog.csdn.net/yidichaxiang/article/details/96429007)


### VNC BK

	sudo apt-get install ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
	sudo apt-get install gnome-core
	
	sudo apt install xfce4 xfce4-goodies tightvncserver
	
	vncserver-virtual -kill :88
	vncserver-virtual :88
	vncserver-virtual :88 -geometry 2240x1260




