### ubuntu16.04 自带pyhon3.5升级到3.6
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.6

# 调整Python3的优先级，使得3.6优先级较高
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2

# 系统python默认为Python2，修改为Python3
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150

PS: python由3.5升级为3.6后，发现用CTRL+ALT+T打不开终端，用桌面终端图标也打不开终端。
解决方法：在/usr/bin/gnome-terminal中将开头的#!/usr/bin/python3改为#!/usr/bin/python3.5

sudo apt install python3.6-tk
sudo apt install libpython3-dev
```

#### 已操作

```py
sudo rm /usr/bin/python3
sudo ln -s python3.5 /usr/bin/python3
```

### 用户目录下安装pip
	wget https://bootstrap.pypa.io/get-pip.py  # 或见附件
	python get-pip.py --user
	# export PATH=~/.local/bin:$PATH

### pip
	sudo apt-get remove python-pip
	sudo apt-get remove python3-pip