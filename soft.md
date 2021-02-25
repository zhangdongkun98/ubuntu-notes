# vim
## vim下载
[addr](https://jingyan.baidu.com/article/046a7b3efd165bf9c27fa915.html)

```sh
sudo apt-get install vim-gtk
sudo vim /etc/vim/vimrc
	添加
		set nu
		set tabstop=4
		set nobackup
		set cursorline
		set ruler
		set autoindent
```

## vim强制保存只读文件

```sh
:w !sudo tee %
```

##vim全选、全部复制、全部删除

	全选（高亮显示）：按esc后，然后ggvG或者ggVG
	全部复制：按esc后，然后ggyG
	全部删除：按esc后，然后dG
	解析：
		gg：是让光标移到首行，在vim才有效，vi中无效 
		v ： 是进入Visual(可视）模式 
		G ：光标移到最后一行 
		选中内容以后就可以其他的操作了，比如： 
		d  删除选中内容 
		y  复制选中内容到0号寄存器 
		"+y  复制选中内容到＋寄存器，也就是系统的剪贴板，供其他程序用


# Sublime Text 3
[安装](https://blog.csdn.net/lu_embedded/article/details/79558280#commentBox)

	官网下载 https://www.sublimetext.com/3
	cd /opt
	sudo tar jxvf ~/下载/sublime_text_3_build_3143_x64.tar.bz2
	./sublime_text_3/sublime_text
	gedit subl
		#!/bin/sh
		exec ~/opt/sublime/sublime_text_3/sublime_text "$@"
	chmod a+x subl
	sudo cp subl /usr/bin/

[自动保存](https://www.cnblogs.com/mzzz/p/6178341.html)


# FireFox

	卸载默认版本
	sudo apt-get purge firefox firefox-locale-en firefox-locale-zh-hans


# Google

[安装](https://blog.csdn.net/weixin_38883338/article/details/82153634)

	（网址）https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
	cd ~/下载
	sudo dpkg -i google-chrome*
	sudo apt-get -f install
	google-chrome
	seahorse


# 安装OpenCV2.4.13.6
[安装](https://blog.csdn.net/chenzhenchou/article/details/79923660)

	（安装编译工具）sudo apt-get install build-essential
	（安装依赖包）sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
	（安装可选包）sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
	下载链接 https://opencv.org/releases.html
	cd ~/下载 
	tar zxvf opencv-2.4.13.6.tar.gz
	cd opencv-2.4.13.6
	mkdir my_build_dir
	cd my_build_dir
	cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
	make -j4
	sudo make install


# 屏幕录制工具Kazam
```bash
sudo apt-get install kazam

# python3.5升级到3.6后无法使用
sudo apt install git virtualenv build-essential python3.6-dev libdbus-glib-1-dev libgirepository1.0-dev
pip3 install dbus-python

#管用
sudo rm /usr/bin/python3
sudo ln -s python3.5 /usr/bin/python3
```

# 视频编辑器
	sudo apt install kdenlive


# Pycharm
[安装](https://www.jianshu.com/p/441d31600647)
[安装与卸载](http://ddrv.cn/a/99888)
[激活码](https://www.jianshu.com/p/e5c0a4a8e6a5)


# 文献管理工具Zotero
[安装](http://www.cogsci.nl/qnotero)
[安装2](https://www.yuanchunrong.com/zotero/)

    sudo add-apt-repository ppa:smathot/cogscinl
    sudo apt-get update
    sudo apt-get install zotero-standalone
    
    或
    https://www.zotero.org/download/
    https://www.zotero.org/support/installation

[111](https://jiangjun.link/post/debian-zotero/)

# Typora
[安装](https://typora.io/#linux)

	wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
	sudo add-apt-repository 'deb https://typora.io/linux ./'
	sudo apt-get update
	sudo apt-get install typora

# OneDrive
[安装](https://github.com/abraunegg/onedrive)

	sudo apt install build-essential
	sudo apt install libcurl4-openssl-dev
	sudo apt install libsqlite3-dev
	sudo apt install pkg-config
	sudo apt install git
	sudo apt install curl
	sudo apt install libnotify-dev
	curl -fsS https://dlang.org/install.sh | bash -s dmd
	
	Run `source ~/dlang/dmd-2.081.1/activate` in your shell to use dmd-2.081.1.
	This will setup PATH, LIBRARY_PATH, LD_LIBRARY_PATH, DMD, DC, and PS1.
	Run `deactivate` later on to restore your environment.
	
	git clone https://github.com/abraunegg/onedrive.git
	cd onedrive
	./configure
	make clean; make;
	sudo make install
	
	proxychains onedrive --synchronize --verbose



# Synergy (与win共享键鼠)

[addr](https://blog.csdn.net/four_stone5/article/details/78075620)

## 安装
```sh
sudo apt-get install synergy
dpkg -l synergy  # 查看版本
# win安装包见附件
```
## 使用

	有键鼠的为server端，先开启server再开启client。
	两台电脑需要在一个局域网捏，并且能够ping通。
	客户端的屏幕需要在服务器端手动添加，开始我以为是可以扫描出来的。
	要注意版本问题。



# 钉钉

[官方包1](http://mirrors.aliyun.com/deepin/pool/non-free/d/dingtalk/)

	sudo dpkg -i dingtalk_2.0.13-145_amd64.deb   # 见附件

[非官方包github](https://github.com/nashaofu/dingtalk/releases)

	dingtalk-2.1.5-latest-amd64.deb  # 见附件
[官方包2](https://blog.csdn.net/qq_40741855/article/details/104750731)

	链接:https://pan.baidu.com/s/1LuDlmZBJvYYWhBBJVsYqhQ 提取码: 2dgg
	dingtalk_1.0.0-2_amd64.deb  或  alibaba.linux.rimet_4.6.33_amd64.deb  # 见附件



# MATLAB

[方法1](https://www.jianshu.com/p/75f263387540)

```bash
mkdir ~/opt/matlab

# 先把第一个iso文件挂载到ubuntu上，然后安装
sudo mount -o loop R2017a_glnxa64_dvd1.iso /home/zdk/opt/matlab
sudo /home/zdk/opt/matlab/install

进入了安装界面,选择用秘钥进行安装
激活码09806-07443-53955-64350-21751-41297

# 到了60%-70%,会提示选择卸载当前的挂载点，选择第二个iso镜像
sudo umount /home/zdk/opt/matlab
cd到iso文件夹
sudo mount -o loop R2017a_glnxa64_dvd2.iso /home/zdk/opt/matlab
这里第二个挂载的镜像要跟第一个挂载的位置要相同，我这里就都是matlab,然后点击继续就可以了

安装完之后我们来进行激活
sudo mkdir /usr/local/MATLAB/R2017a/bin/licenses/ 
cd到iso文件夹
sudo cp license_standalone.lic /usr/local/MATLAB/R2017a/bin/licenses/ 
sudo cp R2017a/bin/glnxa64/libmwservices.so /usr/local/MATLAB/R2017a/bin/glnxa64/
 
sudo umount /home/zdk/opt/matlab
sudo /usr/local/MATLAB/R2017a/bin/matlab
   
sudo chmod 777 /usr/local/MATLAB/R2017a/bin/licenses/

cd ~/.matlab
chmod 777 R2017a
cd ~/.local/share/applications
sudo gedit matlab.desktop
	[Desktop Entry]
    Type=Application
    Name=Matlab
    GenericName=Matlab 2017a
    Comment=Matlab:The Language of Technical Computing
    Exec=sh /usr/local/MATLAB/R2017a/bin/matlab -desktop
	Icon=/usr/local/MATLAB/R2017a/toolbox/nnet/nnresource/icons/matlab.png
    StartupNotify=true
    Terminal=false
    Categories=Development;Matlab;
```



# 搜狗输入法

[blog](https://blog.csdn.net/davidhzq/article/details/102617067)

# VSCode

[VsCode自动生成头部注释和函数注释（无插件，python为例）](https://blog.csdn.net/weixin_44437652/article/details/107720580)

```bash
# https://code.visualstudio.com/下载
sudo apt-get install -f

# pip install flake8
pip install yapf
# 插件：vscode-icons, python, Bracket Pair Colorizer, Better Comments, Markdown All in One, Path Intellisense, Git Lens, Git History, pylance, vscode-pdf
# preference -> color scheme

## settings.json
{
    "workbench.iconTheme": "vscode-icons",
    "python.pythonPath": "/usr/bin/python2.7",
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "yapf",
    "python.languageServer": "Pylance",
    "workbench.colorTheme": "Monokai",
    "files.autoSave": "onFocusChange",
}
```

[Git + VS Code + Overleaf](https://medium.com/@maumneto/git-vs-code-overleaf-91ecfd586b36)


# teamviewer

```bash
# https://www.teamviewer.com/cn/下载/linux/
sudo dpkg -i  teamviewer_13.2.26559_amd64.deb
sudo apt-get install -f
sudo dpkg -i  teamviewer_13.2.26559_amd64.deb
```



# CopyTranslator
[doc](https://copytranslator.github.io/)





# VNC

	sudo apt-get install ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
	sudo apt-get install gnome-core
	
	sudo apt install xfce4 xfce4-goodies tightvncserver
	
	vncserver-virtual -kill :88
	vncserver-virtual :88
	vncserver-virtual :88 -geometry 2240x1260




# OwnCloud  (TODO)

[install](https://www.tecmint.com/install-owncloud-on-ubuntu/)

```bash
sudo apt install apache2 libapache2-mod-php7.2 openssl php-imagick php7.2-common php7.2-curl php7.2-gd php7.2-imap php7.2-intl php7.2-json php7.2-ldap php7.2-mbstring php7.2-mysql php7.2-pgsql php-smbclient php-ssh2 php7.2-sqlite3 php7.2-xml php7.2-zip
sudo dpkg -l apache2
php -v

sudo systemctl start apache2
### check http://localhost/

sudo apt install mariadb-server
sudo mysql_secure_installation

sudo mysql -u root -p
	CREATE DATABASE oc_db_name;
	GRANT ALL ON oc_db_name.* TO 'oc_db_user'@'localhost' IDENTIFIED BY 'yourpassward';
	FLUSH PRIVILEGES;
	EXIT;

sudo wget https://download.owncloud.org/community/owncloud-10.4.0.zip
sudo unzip owncloud-10.4.0.zip -d /var/www/

sudo chown -R www-data:www-data /var/www/owncloud/
sudo chmod -R 755 /var/www/owncloud/

sudo vim /etc/apache2/conf-available/owncloud.conf
	Alias /owncloud "/var/www/owncloud/"

	<Directory /var/www/owncloud/>
	Options +FollowSymlinks
	AllowOverride All

	<IfModule mod_dav.c>
	Dav off
	</IfModule>

	SetEnv HOME /var/www/owncloud
	SetEnv HTTP_HOME /var/www/owncloud

	</Directory>

sudo a2enconf owncloud
sudo a2enmod rewrite
sudo a2enmod headers
sudo a2enmod env
sudo a2enmod dir
sudo a2enmod mime

sudo systemctl restart apache2

### check http://localhost/owncloud/
```

