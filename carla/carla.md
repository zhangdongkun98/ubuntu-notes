## Python API
[addr](https://carla.readthedocs.io/en/latest/python_api/#carlaworld-class)


[Updated the libpng dependency for linux](https://github.com/carla-simulator/carla/pull/1173)

[OpenDrive格式地图数据解析](https://blog.csdn.net/lewif/article/details/78575840#commentBox)




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



conda install 'xerces-c=3.2'