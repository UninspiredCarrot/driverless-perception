Install Docker Desktop
Install an X11 display server

```bash
cd /path/to/folder/with/Dockerfile
xhost +
```

```bash
docker build -t ros:v1 .
docker run -it ros:v1
```

Inside Docker container as `root@xxxxxxxxx:/eufs_folder:\# `

```bash
colcon build
```

Might have to run the above line more than once if you get a similar error:

```bash
c++: fatal error: Killed signal terminated program cc1plus
compilation terminated.
```

```bash
echo 'source /eufs_folder/install/setup.sh' >> ~/.bashrc
source ~/.bashrc
```

And hopefully this next line works:

```bash
ros2 launch eufs_launcher eufs_launcher.launch.py
```