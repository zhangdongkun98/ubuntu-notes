
# ROS Kinetic
[my blog](https://blog.csdn.net/weixin_42315410/article/details/107653495)


# ROS Melodic

```bash
# 安装
sh Miniconda3-latest-Linux-x86_64.sh -b
 
# 初始化命令行
~/miniconda3/bin/conda init
 
# 创建新环境并配置
conda create --name ros_demo -y
conda activate ros_demo
 
conda install python=3.7 pip -y
conda install -c anaconda make
pip install numpy
pip install empy
pip install pyyaml
```

```bash
cd ~/miniconda3/envs/ros_demo/
mkdir pycode && cd pycode
 
# 安装rospkg
git clone https://github.com/ros-infrastructure/rospkg.git
cd rospkg/
python setup.py install
 
# 安装sip
cd ..
# 下载地址 https://riverbankcomputing.com/software/sip/download
cd sip-4.19.25
python configure.py
make
make install

# 安装orocos_kinematics_dynamics
### https://github.com/orocos/orocos_kinematics_dynamics/releases/tag/v1.4.0
### reference: https://github.com/orocos/orocos_kinematics_dynamics/blob/master/orocos_kdl/INSTALL.md
cd orocos_kinematics_dynamics-1.4.0/orocos_kdl
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=~/miniconda3/envs/ros_demo
make
sudo make install
### to uninstall: cat install_manifest.txt | sudo xargs rm
```

```bash
cd ~/miniconda3/envs/ros_demo/
mkdir -p catkin_ws/src && cd catkin_ws/src
 
#下载tf与tf2
git clone -b melodic-devel https://github.com/ros/geometry.git
git clone -b melodic-devel https://github.com/ros/geometry2.git

```

```bash
cd ~/miniconda3/envs/ros_demo/catkin_ws
catkin_make_isolated --cmake-args \
                     -DCMAKE_BUILD_TYPE=Release \
                     -DPYTHON_EXECUTABLE=~/miniconda3/envs/ros_demo/bin/python \
                     -DPYTHON_INCLUDE_DIR=~/miniconda3/envs/ros_demo/include/python3.7m \
                     -DPYTHON_LIBRARY=~/miniconda3/envs/ros_demo/lib/libpython3.7m.so
source ~/miniconda3/envs/ros_demo/catkin_ws/devel_isolated/setup.bash
```

```bash
python -c 'import rospy; print(rospy)'
python -c 'import tf; print(tf)'
```
