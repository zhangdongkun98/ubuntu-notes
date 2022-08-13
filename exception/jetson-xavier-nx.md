

[NX安装与配置](https://www.cnblogs.com/jfchen/)


# 镜像烧录

[web](https://www.balena.io/etcher/)



# 硬件状态——jtop

[Monitor GPU, CPU, and other stats on Jetson Nano / Xavier NX / TX1 / TX2](https://www.seeedstudio.com/blog/2020/07/09/monitor-gpu-cpu-and-other-stats-on-jetson-nano-xavier-nx-tx1-tx2/)

```bash
sudo -H pip3 install -U jetson-stats
sudo systemctl restart jetson_stats.service
jtop
```




# miniforge

[versions](https://github.com/conda-forge/miniforge/releases)

[PyTorch for Jetson](https://forums.developer.nvidia.com/t/pytorch-for-jetson-version-1-10-now-available/72048)


```bash
wget https://github.com/conda-forge/miniforge/releases/download/4.12.0-0/Miniforge-pypy3-4.12.0-0-Linux-aarch64.sh
```


### opencv in python 3.6

[ERROR: Could not build wheels for opencv-python which use PEP 517 and cannot be installed directly](https://stackoverflow.com/questions/63732353/error-could-not-build-wheels-for-opencv-python-which-use-pep-517-and-cannot-be)

```bash
pip install opencv-python==3.4.17.63
```

### pytorch in python 3.6

[issue](https://forums.developer.nvidia.com/t/cannot-install-pytorch/149226) <br>
[issue](https://forums.developer.nvidia.com/t/illegal-instruction-core-dumped/165488) <br>

[pytorch aarch64 release (seems not work)](https://github.com/KumaTea/pytorch-aarch64/releases)


```bash
sudo apt install libopenblas-base libopenmpi-dev

### optional
sudo apt install python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev
### optional
sudo apt install libgeos-dev

pip install numpy==1.19.4

wget https://nvidia.box.com/shared/static/p57jwntv436lfrd78inwl7iml6p13fzh.whl -O torch-1.8.0-cp36-cp36m-linux_aarch64.whl
pip install torch-1.8.0-cp36-cp36m-linux_aarch64.whl
```




# ROS

- install followings before [install ros-melodic](../ROS/ros-melodic-cmd.md)

```bash
sudo apt install python3-minimal
```

