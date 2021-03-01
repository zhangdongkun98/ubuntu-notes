# ubuntu-notes

## default config (16.04)

### desktop 
```bash
sudo apt-get update
sudo apt-get upgrade

sudo apt-get remove unity-webapps-common
sudo apt-get install unity-tweak-tool

sudo add-apt-repository ppa:noobslab/themes
sudo apt-get update
sudo apt-get install flatabulous-theme

sudo add-apt-repository ppa:noobslab/icons
sudo apt-get update
sudo apt-get install ultra-flat-icons
```

### ~/.bashrc
```bash
alias gpu='watch -n 0.3 nvidia-smi'
alias wechat='bash ~/opt/wechat.sh'
alias tb='tensorboard --logdir=. --reload_interval=0.5 --max_reload_threads=8'
alias docker='sudo docker'
```


## default config (18.04)
```bash
sudo apt-get remove update-notifier
sudo apt install gnome-tweak-tool
```


### desktop 
```bash
sudo apt-get update
sudo apt-get upgrade

sudo apt-get remove unity-webapps-common
sudo apt-get install notify-osd
sudo apt-get install unity-tweak-tool

sudo chown $USER:$USER -R /usr/share/themes/
sudo chmod 755 -R /usr/share/themes/
cd /usr/share/themes/
git clone -b 16.04.1 https://github.com/anmoljagetia/Flatabulous

sudo add-apt-repository ppa:noobslab/icons
sudo apt-get update
sudo apt-get install ultra-flat-icons

unity-tweak-tool
```
