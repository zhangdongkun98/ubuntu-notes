

# ssh server

[How do you run a SSH server on Mac OS X?](https://superuser.com/questions/104929/how-do-you-run-a-ssh-server-on-mac-os-x) <br>
- Go to System Preferences -> Sharing, enable Remote Login.






# VLC

[download](https://mirrors.neusoft.edu.cn/videolan/vlc/3.0.16/macosx/vlc-3.0.16-arm64.dmg)


# Scroll Reverser

[web](https://pilotmoon.com/scrollreverser/)

[Mac下独立设置触控板和鼠标的滚动方向](https://www.jianshu.com/p/b14d6d8df099)


# KeyPad

[KeyPad——把 Mac 变成 iPad/iPhone 的蓝牙键盘](https://zhuanlan.zhihu.com/p/330685604) <br>
- Mac App Store


# 搜狗输入法

[web](https://pinyin.sogou.com/mac/)




# 查看电池健康

```bash
ioreg -rn AppleSmartBattery | grep -i capacity
```



# brew

[blog](Mac安装Homebrew的正确姿势)

```bash
/bin/bash -c "$(curl -fsSL https://gitee.com/ineo6/homebrew-install/raw/master/install.sh)"
```



# 系统监控工具 eul

[web](https://github.com/gao-sun/eul)



# CopyTranslator

[web](https://copytranslator.github.io/download/#%E4%B8%8B%E8%BD%BD)

```bash
brew install --cask copytranslator
```



## proxychains-ng (proxychains4)
[addr](https://medium.com/@xiaoqinglin2018/mac-osx-%E4%BD%BF%E7%94%A8proxychains-ng-91ba61472fdf)

```bash
git clone https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng

vim config.mak
    将：
    bindir = /usr/bin
    libdir = /usr/lib
    修改为：
    bindir=/usr/local/bin
    libdir=/usr/local/lib

./configure --prefix=/usr --sysconfdir=/etc
make
sudo make install
sudo make install-config
```



# LaTex

[Mac 安装 LaTeX（MacTeX）](https://blog.csdn.net/u013103952/article/details/108604747)

[Recipe terminated with fatal error: spawn latexmk ENOENT](https://stackoverflow.com/questions/68179318/recipe-terminated-with-fatal-error-spawn-latexmk-enoent) <br>
```bash
sudo chown -R <username> /usr/local/texlive
```


