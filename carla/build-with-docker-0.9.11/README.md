# UE4.24.3, CARLA0.9.11

## 0. Requirements

```
- 64-bit version of Docker in Ubuntu 16.04+.
- Minimum 8GB of RAM
- Minimum 300GB available disk space for building container images
- python3.6 or newer
```

## 1. Build UE4
```bash
pip install ue4-docker
ue4-docker setup
```

```bash
ue4-docker build 4.24.3 --no-engine --no-minimal
```


## 2. Build Carla
**Note: check Content.tar.gz version.**
```bash
docker build -t carla-prerequisites:0.9.11 -f Prerequisites.Dockerfile .
docker build -t carla:0.9.11 -f Carla.Dockerfile .

docker run -it -u root carla:0.9.11 /bin/bash
    apt install vim-gtk
    mkdir -p /home/ue4/carla_server/save/
docker cp ~/carla_server/source/0.9.11/Content.tar.gz ${CONTAINER}:/home/ue4/carla_server/save/
    cd /home/ue4/
    rm -r carla
    git clone -b 0.9.11 https://github.com/carla-simulator/carla.git
    cd carla
    ### modify Update.sh
        function download_content {
            cp /home/ue4/carla_server/save/Content.tar.gz .
            mkdir -p Content
            tar -xvzf Content.tar.gz -C Content
            rm Content.tar.gz
            mkdir -p "$CONTENT_FOLDER"
            mv Content/* "$CONTENT_FOLDER"
            rm -rf Content
            echo "$CONTENT_ID" > "$VERSION_FILE"
            echo "Content updated successfully."
        }
    
    ### modify Util/BuildTools/Package.sh Line 166
        copy_if_changed "./Unreal/CarlaUE4/Plugins/" "${DESTINATION}/Plugins/"

    ./Update.sh
    chown -R ue4:ue4 .
docker commit

docker run -it -u ue4 carla:0.9.11 /bin/bash
    make CarlaUE4Editor
    make PythonAPI
    make build.utils
    make package
    rm -r /home/ue4/carla/Dist
docker commit

```



## 3. Build summit

```
when docker in     add-apt-repo  : do not use —network host !!!

Update.sh need to be rewrite
```


## 4. Usage
[docker-py](https://github.com/docker/docker-py)
```bash
pip install docker

python docker_tools.py --output /output/path
python docker_tools.py --input /assets/to/import/path --output /output/path --packages PkgeName1,PkgeName2

python docker_tools.py -o ~/Downloads --image carla:0.9.11
```


## -1. backup
```bash
docker build \
    --build-arg "HTTP_PROXY=socks5://127.0.0.1:1080/" \
    --build-arg "HTTPS_PROXY=socks5://127.0.0.1:1080/" \
    --network host \
    -t carla:0.9.9.4 -f Carla.Dockerfile .
docker build --network host -t carla:0.9.9.4 -f Carla.Dockerfile .
docker run -it --network host -m 12g carla:0.9.9.4 /bin/bash
docker run -it -u ue4 --env HTTP_PROXY="http://127.0.0.1:1080" --env HTTPS_PROXY="https://127.0.00.1:1080" --net host carla:0.9.9.4 /bin/bash
docker run -it -u ue4 --net host carla:0.9.9.4 /bin/bash

./docker_tools.py --input ~/Documents/test_roadrunner/Exports/ --output ~/Documents/output --packages map_package
```


