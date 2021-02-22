## Python API
[addr](https://carla.readthedocs.io/en/latest/python_api/#carlaworld-class)


[Updated the libpng dependency for linux](https://github.com/carla-simulator/carla/pull/1173)

[OpenDrive格式地图数据解析](https://blog.csdn.net/lewif/article/details/78575840#commentBox)



## 安装
寻找硬盘中的附件

	NVIDIA驱动，在右上角设备中查看 图形，若与显卡型号一致则正常
	
	技巧：翻墙；利用服务器git clone，然后scp到本地
	
	Update.sh修改  



## ROS bridge
	#setup folder structure*
	mkdir -p ~/carla-ros-bridge/catkin_ws/src
	cd ~/carla-ros-bridge
	git clone https://github.com/carla-simulator/ros-bridge.git
	cd catkin_ws/src ln -s ../../ros-bridge
	source /opt/ros/kinetic/setup.bash *#Watch out, this sets ROS Kinetic.*
	cd ..
	*#install required ros-dependencies*
	rosdep update
	rosdep install --from-paths src --ignore-src -r *#build* catkin_make

