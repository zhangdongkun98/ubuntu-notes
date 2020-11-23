# Install

[blog](https://blog.csdn.net/jinking01/article/details/82490688)

```bash
sudo apt-get remove docker docker-engine docker-ce docker.io
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce
systemctl status docker
sudo systemctl start docker
sudo docker run hello-world
```

[a bug](https://www.digitalocean.com/community/questions/how-to-fix-docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket)

	sudo chmod 666 /var/run/docker.sock



[proxy](https://note.qidong.name/2020/05/docker-proxy/)



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







# 删除容器

可以使用 `docker container rm` 来删除一个处于终止状态的容器。例如



```
$ docker container rm  trusting_newton
trusting_newton
```

如果要删除一个运行中的容器，可以添加 `-f` 参数。Docker 会发送 `SIGKILL` 信号给容器。

# 清理所有处于终止状态的容器

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





docker run -it --rm  carla:latest /bin/bash