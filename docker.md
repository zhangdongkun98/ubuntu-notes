# Install

### 1. for ubuntu

[blog](https://blog.csdn.net/jinking01/article/details/82490688)

```bash
sudo apt-get remove docker docker-engine docker-ce docker.io
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update

### for 18.04
curl -O https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/containerd.io_1.4.3-1_amd64.deb
sudo apt install ./containerd.io_1.4.3-1_amd64.deb

apt-cache madison docker-ce

sudo apt-get install -y docker-ce

systemctl status docker
sudo systemctl start docker
sudo docker run hello-world
```

### 1. for mac

[Mac下安装docker的三种方法](https://zhuanlan.zhihu.com/p/91116621)

https://hub.docker.com/editions/community/docker-ce-desktop-mac



### 2. 用户加入docker组

```bash
sudo groupadd docker

# 应用用户加入docker用户组
sudo usermod -aG docker ${USER}

# 重启docker服务
sudo systemctl restart docker

# 切换或者退出当前账户再从新登入
su root             # 切换到root用户
su ${USER}          # 再切换到原来的应用用户以上配置才生效
```


### 安装 nvidia-docker (deprecated)
```bash
# 清理以前的。If you have nvidia-docker 1.0 installed: we need to remove it and all existing GPU containers
sudo docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f
sudo apt-get purge -y nvidia-docker
sudo apt autoremove
 
# 执行命令。Add the package repositories
# command 1
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
  sudo apt-key add -
 
# command 2
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
 
# command 3
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update
 
# 正式安装。Install nvidia-docker2 and reload the Docker daemon configuration
sudo apt-get install -y nvidia-docker2
sudo pkill -SIGHUP dockerd
 
# 测试一下。 Test nvidia-smi with the latest official CUDA image
docker run -v /usr/local/nvidia//:/usr/local/nvidia -it --rm --gpus all nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04 bash
docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
```

### 3. 安装 nvidia-docker2

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html

```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update
sudo apt-get install -y nvidia-docker2

docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi

```

### A bug (deprecated)

[a bug](https://www.digitalocean.com/community/questions/how-to-fix-docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket)

	sudo chmod 666 /var/run/docker.sock

# docker默认存储位置
```bash
sudo service docker stop
sudo mv /var/lib/docker /media/ff/Gold/docker
sudo ln -s /media/ff/Gold/docker /var/lib/docker
sudo service docker start

### or

cat /etc/docker/daemon.json

{
   "graph": "/data/docker"
}

sudo systemctl daemon-reload
sudo systemctl restart docker.service

docker info | grep Root
```


# docker源 (todo)
```bash
cat /etc/docker/daemon.json

{
   "runtimes": {
      "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
      }
   }
}
```

[proxy](https://note.qidong.name/2020/05/docker-proxy/)


# use cuda in docker

```bash
apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
git clone https://gitlab.com/nvidia/container-images/cuda.git
```



# 常用命令 (todo)


1. 查看所有正在运行容器
   `docker ps`
2. 查看所有容器
   `docker ps -a`
3. 查看所有容器ID
   `docker ps -a -q`
4. 停止某个具体容器
   `docker stop 容器ID`
5. stop停止所有容器
   `docker stop $(docker ps -a -q)`
6. remove删除容器
   `docker rm 容器ID`
7. remove删除所有容器
   `docker rm $(docker ps -a -q)`
8. ps查询所有镜像
   `docker images`
9. rmi删除镜像
   `docker rmi 前面查询到的镜像id`
10. stop停止镜像运行
    `docker stop id或者run命令所起的名字`
11. 重启容器
   `docker restart cid`


```bash
sudo systemctl disable docker.service docker.socket
```

### 删除容器

可以使用 `docker container rm` 来删除一个处于终止状态的容器。例如



```
$ docker container rm  trusting_newton
trusting_newton
```

如果要删除一个运行中的容器，可以添加 `-f` 参数。Docker 会发送 `SIGKILL` 信号给容器。

### 清理所有处于终止状态的容器

用 `docker container ls -a` 命令可以查看所有已经创建的包括终止状态的容器，如果数量太多要一个个删除可能会很麻烦，用下面的命令可以清理掉所有处于终止状态的容器。



```
$ docker container prune
```







docker cp :用于容器与主机之间的数据拷贝。
1、从主机往容器中拷贝
eg：将主机/www/runoob目录拷贝到容器96f7f14e99ab的/www目录下。

```
docker cp /www/runoob 96f7f14e99ab:/www/1
```

2、将容器中文件拷往主机
eg：将容器96f7f14e99ab的/www目录拷贝到主机的/tmp目录中。

```
docker cp  96f7f14e99ab:/www /tmp/1
```

eg:将主机/www/runoob目录拷贝到容器96f7f14e99ab中，目录重命名为www。

```
docker cp /www/runoob 96f7f14e99ab:/www
```

```bash
docker run -it --rm  carla:latest /bin/bash
```







# 应用
### 微信
[手把手教你在Ubuntu 20.04上通过docker安装微信和QQ](https://zhuanlan.zhihu.com/p/323723229)
```bash
xhost +
docker pull bestwu/wechat

docker run -d --name wechat --device /dev/snd --ipc=host \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-v $HOME/WeChatFiles:/WeChatFiles \
-e DISPLAY=unix$DISPLAY \
-e XMODIFIERS=@im=fcitx \
-e QT_IM_MODULE=fcitx \
-e GTK_IM_MODULE=fcitx \
-e AUDIO_GID=`getent group audio | cut -d: -f3` \
-e GID=`id -g` \
-e UID=`id -u` \
bestwu/wechat
```

### owncloud
```bash
docker pull owncloud
docker pull mysql:5.7

docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=密码 -d mysql:5.7
docker run --name owncloud --link some-mysql:mysql -d owncloud:latest

docker run -d -p 80:80 owncloud:latest
```
