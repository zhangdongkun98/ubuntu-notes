# ubuntu-notes

## Guide

[命令行翻墙](./net.md#proxychains-ng-proxychains4) <br>

[显卡驱动(cuda 11.0)](./graphics.md#cuda-toolkit-110-download) <br>




## default config (16.04)

### desktop
```bash
sudo apt update
sudo apt upgrade

sudo apt remove unity-webapps-common
sudo apt install unity-tweak-tool

sudo add-apt-repository ppa:noobslab/themes
sudo apt update
sudo apt install flatabulous-theme

sudo add-apt-repository ppa:noobslab/icons
sudo apt update
sudo apt install ultra-flat-icons
```

### ~/.bashrc
```bash
alias gpuog='watch -n 0.3 nvidia-smi'
alias gpu='watch -n 0.3 "python3 ~/opt/nvidia-htop/nvidia-htop.py -l 100"'
alias wechat='bash ~/opt/wechat.sh'
alias tb='tensorboard --logdir=. --reload_interval=0.5 --max_reload_threads=8'
alias condaa='conda activate'
alias condad='conda deactivate'
alias opn='code ~/github/zdk/ubuntu-notes'
alias yg='proxychains4 you-get'
alias route='sudo bash /etc/rc.local'
alias gtt='git status'
alias gd='git diff'
```


## default config (18.04)

- 选择minimal installation

```bash
sudo apt remove update-notifier
sudo apt install gnome-tweak-tool
```


### desktop
```bash
sudo apt update
sudo apt upgrade

sudo apt remove unity-webapps-common
sudo apt install notify-osd
sudo apt install unity-tweak-tool

sudo chown $USER:$USER -R /usr/share/themes/
sudo chmod 755 -R /usr/share/themes/
cd /usr/share/themes/
git clone -b 16.04.1 https://github.com/anmoljagetia/Flatabulous

sudo add-apt-repository ppa:noobslab/icons
sudo apt update
sudo apt install ultra-flat-icons

unity-tweak-tool
```


## default config (mac)

```bash
chsh -s /bin/bash
```

```bash
### install vscode
### 打开VSCode –> command+shift+p –> 输入shell command –> 点击提示Shell Command: Install ‘code’ command in PATH运行
```
