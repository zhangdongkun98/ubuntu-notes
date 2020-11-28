## planner_ws使用
	ros-kinetic
	sudo apt-get install ros-kinetic-navigation
	
	mkdir ~/mycarla
	cd ~/mycarla
	scp liulu@10.13.22.251:~/carla/carla_0.9.5/PythonAPI/carla/dist/carla-0.9.5-py2.7-linux-x86_64.egg .
	scp -r liulu@10.13.22.251:~/carla/carla_0.9.5/PythonAPI/examples .
	
	# 存疑
	sudo apt-get install libpng16-dev
	sudo apt-get install libpng16*
	
	pip install pygame
	pip install 'networkx==2.2'
	
	sudo apt-get install ros-kinetic-teb-local-planner
	
	echo "export PYTHONPATH=/home/zdk/mycarla/carla-0.9.5-py2.7-linux-x86_64.egg" >> ~/.bashrc


## 安装
```bash
sudo apt-get install ros-kinetic-rqt-controller-manager
```

