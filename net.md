




# 科学上网



## 命令行翻墙：proxychains-ng (proxychains4)
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


## clashy

[addr](https://github.com/SpongeNobody/Clashy/releases)



## SS (deprecated)
[安装](https://zhoukay.top/2018/09/16/Ubuntu16-04%E9%85%8D%E7%BD%AEshadowsocks-qt5%E5%AE%A2%E6%88%B7%E7%AB%AF/)

```sh
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt-get update
sudo apt-get install shadowsocks-qt5
```

## ssr (deprecated)
[addr1](https://mumumushi.github.io/2018/09/06/use_ssr_in_Linux/) <br>
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
## electron-ssr (deprecated)

[原址](https://github.com/chenchaohan/electron-ssr) <br>
[备份](https://github.com/qingshuisiyuan/electron-ssr-backup) <br>
[dependency](https://github.com/qingshuisiyuan/electron-ssr-backup/blob/master/Ubuntu.md) <br>

```sh
sudo apt-get -f install libappindicator1 libindicator7
见附件
```



# 连接科学上网端口

- apt
```bash
sudo apt update -o Acquire::http::proxy="http://127.0.0.1:2340/"
```


# 校外网VPN

```bash
sudo apt install network-manager-l2tp network-manager-l2tp-gnome
```



# 使用国内镜像服务器，解决apt-get、pip等安装工具下载依赖包速度慢的问题 (deprecated)
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




