# use Docker

```
# TODO
Prerequisites.Dockerfile
apt install libboost-dev libbz2-dev

check ue4 version:
1. Unreal/CarlaUE4/CarlaUE4.uproject

check Content.tar.gz version



make CarlaUE4Editor
make PythonAPI
make build.utils
make package


rm -r /home/ue4/carla/Dist
```





## summit



```
cp CustomAssets/EmptyMap.umap Unreal/CarlaUE4/Content/Carla/Maps/TestMaps/EmptyMap.umap
cp CustomAssets/EmptyMap_BuiltData.uasset Unreal/CarlaUE4/Content/Carla/Maps/TestMaps/
cp CustomAssets/M_Tile.uasset Unreal/CarlaUE4/Content/Carla/Static/GenericMaterials/Ground/
```

when docker in     add-apt-repo  : do not use —network host !!!