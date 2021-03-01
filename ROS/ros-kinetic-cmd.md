## 安装
[addr](https://blog.csdn.net/tq08g2z/article/details/79209435)

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F42ED6FBAB17C654
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
sudo rosdep init
rosdep update
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential
```

## 测试程序---小海龟
[addr](https://blog.csdn.net/qq_17232031/article/details/79519308)

	sudo apt-get install ros-kinetic-turtlesim
	roscore
	rosrun turtlesim turtlesim_node
	rosrun turtlesim turtle_teleop_key

## ROS kinetic 创建工作空间
[addr](https://blog.csdn.net/youshijian99/article/details/79924016)

	~$ mkdir -p ~/catkin_ws/src
	~/catkin_ws/src$ catkin_init_workspace
	~/catkin_ws$ catkin_make
	vim ~/.bashrc
		添加source /home/zdk/catkin_ws/devel/setup.bash

## 环境变量
	echo $ROS_PACKAGE_PATH
	source devel/setup.bash
	source ~/catkin_ws/devel/setup.bash

## ROS in python3
	sudo apt-get install python3-yaml
	pip3 install rospkg catkin_pkg



## 可视化话题与节点

	rosrun rqt_graph rqt_graph

## 启动gazebo
	roscore & rosrun gazebo_ros gazebo
	roslaunch gazebo_ros empty_world.launch

## gazebo下载模型
[addr](https://blog.csdn.net/qq_40213457/article/details/81021562)

	gazebo
	cd ~/.gazebo/
	mkdir -p models
	cd ~/.gazebo/models/
	wget http://file.ncnynl.com/ros/gazebo_models.txt
	wget -i gazebo_models.txt
	ls model.tar.g* | xargs -n1 tar xzvf

## VMware: vmw_ioctl_command error 无效的参数
[addr](https://blog.csdn.net/coolwaterld/article/details/72467942)

	echo "export SVGA_VGPU10=0" >> ~/.bashrc
	reboot

## gazebo7升级到gazebo9
[addr1](http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install)
[addr2](https://blog.csdn.net/zhangrelay/article/details/74356137)

	sudo apt-get remove gazebo7 gazebo7-common gazebo7-plugin-base libgazebo7:amd64 libgazebo7-dev:amd64
	sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
	cat /etc/apt/sources.list.d/gazebo-stable.list
		deb http://packages.osrfoundation.org/gazebo/ubuntu-stable xenial main
	wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install gazebo9
	sudo apt-get install libgazebo9-dev
	gazebo
	sudo apt-get install ros-kinetic-gazebo9-*
	roslaunch gazebo_ros empty_world.launch

## 安装gazebo7
[addr](https://www.linuxidc.com/Linux/2017-03/141505.htm)

	rm /etc/apt/sources.list.d/gazebo-stable.list
	sudo apt-get update
	sudo apt-get install gazebo7
	sudo apt-get install libgazebo7-dev
	gazebo
	sudo apt-get install ros-kinetic-gazebo-*

## 安装turtlebot

	sudo apt-get install pyqt5-dev-tools pyqt4-dev-tools
	https://blog.csdn.net/qq_37427972/article/details/82850177#commentBox
	https://blog.csdn.net/Discoverhfub/article/details/79719937
	
	Gazebo版本问题，这个我不是很确定，但默认自带的Gazebo7.0折腾了我很久，刚一运行没多久，再运行个rviz，就很容易崩，我觉得可能是Gazebo很占资源，加上本人笔记本不算快，再同时运行rviz、gmapping等节点，导致Gazebo不太稳定，但是，我升级了Gazebo7.11.0后，同样的操作，程序意外结束的情况就变得很少了！如果你的Gazebo也常常意外终止，可以考虑一下换个版本。
	原文链接：https://blog.csdn.net/lingchen2348/article/details/79503970


​	
​	https://stackoverflow.com/questions/39281644/ros2-importerror-no-module-named-genmsg
​	This happens while dependencies installed for ROS and ROS2 on the same machine. Especially the package python-genmsg and ros-kinetic-genmsg. genmsg can now found at these places:
​	
​	    /opt/ros/kinetic/lib/python2.7/dist-packages
​	    /usr/lib/python2.7/dist-packages


​	
​	https://www.ncnynl.com/archives/201609/792.html

## gazebo环境使用husky小车
[addr1](https://www.jianshu.com/p/1ff86addefdc)
[addr2](https://github.com/TaarLab/husky_joy)

	sudo apt-get update
	sudo apt-get install ros-kinetic-husky-desktop
	sudo apt-get install ros-kinetic-husky-simulator
	git clone https://github.com/TaarLab/husky_joy.git
	catkin_make -DCATKIN_WHITELIST_PACKAGES="husky_joy"
	(In launch directory)$ roslaunch husky_joy.launch
	rostopic pub -r 10 /cmd_vel geometry_msgs/Twist '{linear: {x: 0.5, y: 0, z: 0}, angular: {x: 0, y: 0, z: 0.5}}'

## 检查URDF语法
​	sudo apt-get install liburdfdom-tools
​	（urdf可视化）urdf_to_graphiz my_robot.urdf
​	（xacro转urdf）rosrun xacro xacro urdf/GRobot.xacro --inorder > GRobot.urdf
​	check_urdf my_robot.urdf
​	rosrun urdfdom check_urdf /tmp/pr2.urdf

## 安装docker
[addr1](https://jingyan.baidu.com/article/0aa223756cf6e388cc0d6412.html)
[addr2](https://blog.csdn.net/jinking01/article/details/82490688#commentBox)

	sudo apt-get remove docker docker-engine docker-ce docker.io
	sudo apt-get update
	sudo apt-get install docker
	sudo apt-get install docker.io
	sudo apt-get install docker-registry
	sudo systemctl start docker
	systemctl status docker
	sudo docker run hello-world

## ROS python
​	https://blog.csdn.net/light_jiang2016/article/details/55505627
​	https://blog.csdn.net/Cyril__Li/article/details/78979253

	https://blog.csdn.net/wuguangbin1230/article/details/78422393
	ROS Twist和Odometry消息类型使用（Python）
	https://www.cnblogs.com/shang-slam/p/6891086.html
	
	https://blog.csdn.net/bluewhalerobot/article/details/80952776

## Docker中Temporary failure resolving 'archive.ubuntu.com'等报错
[addr](http://www.voidcn.com/article/p-xnbryzwk-bqt.html)

	sudo vim /etc/resolv.conf
		添加nameserver 192.168.149.2 （该地址为Ubuntu虚拟机上system网络中的DNS，查看连接信息可获得）

## docker: Error response from daemon:

## nvidia docker报错
​	add-apt-repository ppa:graphics-drivers/ppa
​	apt update
​	apt install nvidia-410

## ignition相关命令（gazebo9中无需）
​	sudo apt remove libignition-math2 libsdformat4
​	sudo apt-get install libignition-math3 libsdformat5
​	sudo apt-get install libignition-transport4 libignition-transport4-dev libignition-msgs0-dev

## 安装anaconda3（python3.6.5）
[addr](https://blog.csdn.net/ITBigGod/article/details/85690257)

	从https://repo.anaconda.com/archive/下载Anaconda3-5.2.0-Linux-x86_64.sh
	cd ~/下载
	bash Anaconda3-5.2.0-Linux-x86_64.sh
	source ~/.bashrc



# carla相关
​	**need google**
​	https://www.litcc.com/2016/12/29/Ubuntu16-shadowsocks-pac/index.html
​	https://zhoukay.top/2018/09/16/Ubuntu16-04%E9%85%8D%E7%BD%AEshadowsocks-qt5%E5%AE%A2%E6%88%B7%E7%AB%AF/
​	https://blog.csdn.net/qq_31239495/article/details/80565401
​	https://www.koalazb.com/blogs/370/

	https://blog.csdn.net/wolf96/article/details/82557328
	https://github.com/EpicGames/UnrealEngine
	https://github.com/carla-simulator/carla
	https://carla.readthedocs.io/en/stable/how_to_build_on_linux/
	https://wiki.unrealengine.com/Building_On_Linux
	https://github.com/EpicGames/Signup
	**important**
	https://blog.csdn.net/davidhopper/article/details/81485872#commentBox
	http://www.sohu.com/a/257396295_100285120
	
	https://blog.csdn.net/sinat_25882019/article/details/81006619
	https://blog.csdn.net/xmy306538517/article/details/79412109
	https://blog.csdn.net/davidhopper/article/details/81485872#commentBox
	https://blog.csdn.net/ccc15327311512/article/details/89196241
	https://blog.csdn.net/yanglei_1993/article/details/90299786
	https://blog.csdn.net/weixin_39059031/article/details/84028487



# TORCS相关
## 安装MuJoCo
[addr](https://blog.csdn.net/will_ye/article/details/81087463#commentBox)
[addr](https://github.com/openai/mujoco-py#obtaining-the-binaries-and-license-key)

	mkdir ~/.mujoco
	cp mujoco200_linux.zip ~/.mujoco
	cd ~/.mujoco
	unzip mujoco200_linux.zip
	cp mjkey.txt ~/.mujoco
	cp mjkey.txt ~/.mujoco/ mujoco200/bin
	gedit ~/.bashrc
		添加
			export LD_LIBRARY_PATH=~/.mujoco/ mujoco200/bin${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
			export MUJOCO_KEY_PATH=~/.mujoco${MUJOCO_KEY_PATH}
	cd ~/.mujoco/ mujoco200/bin
	./simulate ../model/humanoid.xml

## 安装mujoco_py
[addr1](https://github.com/openai/mujoco-py#obtaining-the-binaries-and-license-key)
[addr2](https://blog.csdn.net/jianghao_ava/article/details/80874254)

	conda create -n mujoco-py python=3.6 numpy
	cd
	git clone https://github.com/openai/mujoco-py.git
	cd ~/mujoco-py
	cp requirements.txt requirements.dev.txt mujoco_py
	cd mujoco_py
	pip install -r requirements.txt
	pip install -r requirements.dev.txt

## 安装gym
[addr1](https://blog.csdn.net/will_ye/article/details/81087463#commentBox)
[addr2](https://github.com/openai/gym#testing)

	cd
	git clone https://github.com/openai/gym.git
	cd gym
	apt-get install -y python-numpy python-dev cmake zlib1g-dev libjpeg-dev xvfb libav-tools xorg-dev python-opengl libboost-all-dev libsdl2-dev swig
	pip install -e .[all]

## 安装Gym-TORCS
[addr1](https://github.com/ugo-nama-kun/gym_torcs)
[addr2](https://blog.csdn.net/wgbarry/article/details/82827981)
[addr3](https://www.jianshu.com/p/f3bdf74ac21c)

	cd
	git clone https://github.com/ugo-nama-kun/gym_torcs.git
	cd ~/gym_torcs/vtorcs-RL-color
	sudo apt-get install libglib2.0-dev libgl1-mesa-dev libglu1-mesa-dev freeglut3-dev libplib-dev libopenal-dev libalut-dev libxi-dev libxmu-dev libxrender-dev libxrandr-dev libpng12-dev
	./configure
	make
	sudo make install
	sudo make datainstall
	sudo torcs
		依次点击Race/Practice/New Race，启动服务器。
	cd ~/gym_torcs
	python snakeoil3_gym.py


## rosclean
	rosclean check
	rosclean purge


## tmp
	sudo apt-get install ros-kinetic-husky-navigation ros-kinetic-husky-gazebo ros-kinetic-husky-viz
	
	roslaunch husky husky_gazebo.launch
	roslaunch husky_viz view_robot.launch
	roslaunch husky_navigation gmapping_demo.launch


​	
​	rosrun map_server map_server /home/zdk/tmp/aaaa.yaml
​	
​	rosrun turtlesim turtle_teleop_key /turtle1/cmd_vel:=/cmd_vel
​	rosrun map_server map_saver -f testpic
​	rosrun keyboard_control keyboard_control
