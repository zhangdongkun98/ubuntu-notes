## su认证失败
[addr](https://blog.csdn.net/heyangweng/article/details/53728056)

	sudo passwd root



## 进程

[addr](https://www.cnblogs.com/wybliw/p/10237648.html)

	暂停进程Ctrl+Z
	继续进程fg



## 显示历史命令

	history



## 压缩与解压命令

[addr](https://www.cnblogs.com/sinsenliu/p/9369729.html)

```bash
# 解压
tar zxvf filename.tar.gz
unzip
# 压缩
tar zcvf FileName.tar.gz DirName

# 批量解压
for tar in *.tar; do tar xvf $tar; done
find . -name '*.zip' -exec unzip {} \;
find . -name '*.zip' -exec unzip -n -d /target/dir {} \;
```


## 查看文件夹大小
[du命令](https://blog.csdn.net/ouyang_peng/article/details/10414499)

	du -h --max-depth=1

## 查看目录下文件个数
[blog](https://blog.csdn.net/xh_hit/article/details/80651565)

	ls -l|grep "^-"| wc -l

## 打开文件管理器

	nautilus

## git

### create new repo
```bash
# create a new repository on the command line
echo "# d2l-en" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/zhangdongkun98/ubuntu-notes.git
git push -u origin master
```

### pull all branches
```bash
git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
git fetch --all
git pull --all
```

### remove all history commits

```bash
git checkout --orphan new-history
git add -A
git commit -m "Initial commit"
git branch -D main  # or the main branch you're working with
git branch -m main
git push -f origin main
```


### 回退特定文件

```bash
git checkout <commit> <filename>
```



### 根据tag创建分支

```bash
git branch <new-branch-name> <tag-name>
git push origin <new-branch-name>
```


### git-lfs

[doc](https://git-lfs.github.com/)
[package](https://github.com/git-lfs/git-lfs/releases)
[安装](https://blog.csdn.net/anlian523/article/details/100520039)


```bash
# 从https://github.com/git-lfs/git-lfs/releases下载二进制文件（见附件）
tar -xzvf git-lfs-linux-amd64-v2.10.0.tar.gz
sudo ./install.sh

git lfs install
git lfs track "*.psd"
git add .gitattributes
git add file.psd
git commit -m "Add design file"
git push origin master
```





## 查看端口

    lsof -i:port
    lsof -i



## 查看CPU型号

```bash
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
```


## gpu
```bash
git clone https://github.com/peci1/nvidia-htop.git
./nvidia-htop.py
```
