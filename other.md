# cuda
[addr1](https://blog.csdn.net/u014380165/article/details/77340765)

# python
## matplotlib
[Python数据可视化matplotlib.pyplot](https://www.jianshu.com/p/85a01b7d6507)

## Jupyter Notebook
[安装与配置](https://blog.csdn.net/qq_42881421/article/details/88070832)

	sudo apt-get update
	pip3 install jupyter
	jupyter notebook --generate-config
	ipython
		在In[1]一行输入如下语句
		In [1]: from notebook.auth import passwd
		 
		输入两次一样的密码，以后浏览器登录jupyter用得到
		In [2]: passwd()
		Enter password:
		Verify password:
		Out[2]: 'sha1:7e07e7fe86be:f5b3b8f2b30a1b0f7586b0ddf08b8dd836a9bf00'
		复制Out[2]的输出
	gedit ~/.jupyter/jupyter_notebook_config.py
		在文件末尾增加
		c.NotebookApp.password = u'sha1:XXXXXX'
		注意：sha1:xxxxxx，要换成刚才从Out[2]复制到的内容
	jupyter notebook --ip=0.0.0.0 --no-browser --allow-root


##改变pip指向
[addr](https://blog.csdn.net/u012516318/article/details/75339860)

	which pip
		/home/zdk/.local/bin/pip
	vim /home/zdk/.local/bin/pip
		将第一行 #!/usr/bin/python3 修改为 #!/usr/bin/python2
