# CPU
```bash
查看CPU频率
cat /proc/cpuinfo |grep MHz|uniq
sudo cat /sys/devices/system/cpu/cpu*/cpufreq/cpuinfo_cur_freq

# 温度
https://github.com/fossfreedom/indicator-sysmonitor/tree/master

# 百分百负载
for i in `seq 1 $(cat /proc/cpuinfo |grep "physical id" |wc -l)`; do dd if=/dev/zero of=/dev/null & done
	说明:
        cat /proc/cpuinfo |grep "physical id" | wc -l 可以获得CPU的个数, 我们将其表示为N.
        seq 1 N 用来生成１到Ｎ之间的数字
        for i in `seq 1 N`; 就是循环执行命令,从１到Ｎ
        dd if=/dev/zero of=/dev/null 执行dd命令, 输出到/dev/null, 实际上只占用CPU, 没有IO操作.
        由于连续执行Ｎ个(Ｎ是ＣＰＵ个数)的dd 命令, 且使用率为１００%, 这时调度器会调度每个dd命令在不同的CPU上处理.
        最终就实现所有ＣＰＵ占用率１００%
        另外，上述程序的结束可以使用：
        1. fg 后按 ctrl + C (因为该命令是放在后台执行)
        2. pkill -9 dd

```


# 硬盘
## exfat

```bash
sudo apt-get install exfat-fuse exfat-utils
```

## 挂载/卸载

[addr](https://blog.csdn.net/u012348774/article/details/79108544)

```bash
sudo fdisk -l
	/dev/sdb4
sudo mount -t vfat /dev/sdb4 /media/zdk
	//-t 后的vfat是文件系统格式，即FAT32
	//dev/sdb4是需要挂载的U盘
	//media/zdk是挂载点

sudo umount /dev/sdb4
```

## 查看磁盘
	lsblk

cha kan sheng yu kong jian

```
df -hl
```


# 网卡
## TP-LINK 无线网卡（TL-WDN5200H免驱版）安装驱动
[blog](https://zhuanlan.zhihu.com/p/214136483)

	git clone https://github.com/brektrou/rtl8821CU.git
	
	make
	sudo make install
	sudo modprobe 8821cu
	lsusb （用于查看网卡，得到的结果里应该有0bda:1a2b）
	sudo usb_modeswitch -KW -v 0bda -p 1a2b
	sudo systemctl start bluetooth.service

	make clean  ## if rebuild

	### for 18.04
	chmod +x dkms-install.sh
	sudo ./dkms-install.sh
	sudo modprobe 8821cu


## 双网卡上网

[blog](https://blog.csdn.net/dajiangqingzhou/article/details/82901666)

	subl /etc/rc.local
		route add -net 0.0.0.0/0 wlx5475950277bd
        route add -net 0.0.0.0/0 gw 192.168.31.1
        route add -net 10.0.0.0/8 enp7s0
        route add -net 10.0.0.0/8 gw 10.12.120.1
	reboot


# 声卡

```bash
sudo apt install pavucontrol
```
