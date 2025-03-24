
# 启用虚拟显示器
通过配置虚拟显示器，可以让系统模拟一个显示器的存在，即使没有实际的物理显示器连接。

步骤 1：安装虚拟显示器工具
使用 xrandr 和 xserver-xorg-video-dummy 创建虚拟显示器。

```bash
sudo apt update
sudo apt install xserver-xorg-video-dummy
```

步骤 2：创建 Xorg 配置文件
创建一个新的 Xorg 配置文件以启用虚拟显示器。

```bash
sudo vim /usr/share/X11/xorg.conf.d/10-dummy.conf
```

添加以下内容：

```conf
Section "Device"
    Identifier "DummyDevice"
    Driver "dummy"
    VideoRam 256000
EndSection

Section "Screen"
    Identifier "DummyScreen"
    Device "DummyDevice"
    Monitor "DummyMonitor"
    DefaultDepth 24
    SubSection "Display"
        Depth 24
        Modes "1920x1080"  # 设置你希望的分辨率
    EndSubSection
EndSection

Section "Monitor"
    Identifier "DummyMonitor"
    HorizSync 28.0-80.0
    VertRefresh 48.0-75.0
    ModeLine "1920x1080" 173.00 1920 2048 2248 2576 1080 1083 1088 1120 -hsync +vsync
EndSection
```

保存并退出。

步骤 3：重启显示服务
重启 Xorg 服务以应用更改：

```bash
sudo systemctl restart display-manager
```
此时，系统会模拟一个虚拟显示器，即使没有外接显示器，桌面环境也会正常运行。
