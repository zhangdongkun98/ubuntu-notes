# VNC


[Ubuntu18.04 LTS 安装 VNC Server](https://blog.csdn.net/yidichaxiang/article/details/96429007)
[Ubuntu18.04 LTS 安装 VNC Server[x11vnc,tightvncserver,vnc4server]](https://blog.csdn.net/yidichaxiang/article/details/100533237#commentBox)


sudo apt install xfce4 xfce4-goodies xorg dbus-x11 x11-xserver-utils
sudo apt install tigervnc-standalone-server tigervnc-common

sudo apt install tigervnc-standalone-server tigervnc-common tigervnc-xorg-extension tigervnc-viewer

sudo apt-get install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
sudo apt-get install --no-install-recommends ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal gnome-core



netstat -anp
netstat -tulpn


```bash
# 从https://dl.bintray.com/tigervnc/stable/ubuntu-16.04LTS/amd64/下载
tigervncserver_1.7.0-1ubuntu1_amd64.deb
```


sudo apt-get purge realvnc-vnc-server
sudo apt-get purge realvnc-vnc-viewer


vncserver -geometry 2560x1440 -depth 32
ssh zdk@10.12.120.46 -L 5901:127.0.0.1:5901


## ~/.vnc/xstartup
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