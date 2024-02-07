# Docker Instructions

## Installing Docker

1. Install [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)
2. Login to Docker from the Desktop App
3. Check it works with `docker run hello-world`


## Using Images

- List all images: `docker image ls`
- Pull image: `docker image pull <image-name>:<tag>`
- Delete image: `docker image rm -f <image-name>`
    - *the `-f` is for forcing this delete, without it, docker won't delete the image if u have any containers that were created from it*
- Build image from dockerfile: `docker image build -t <image-name> <path/to/folder/with/Dockerfile>`

## Using Containers

- List all containers: `docker ps -a`
- Stop container: `docker container stop <container-name>`
- Start a stopped container: `docker container start -i <container-name>`
- Delete a container: `docker container rm <container-name>`
- Remove all stopped containers: `docker container prune`
- Run a command on an already running container: `docker exec -it <container-name> <command>`
    - if `<command>` is `bin/bash` then it will give you a new terminal to interact with the container
-

### Running a container
Run container from image: `docker run <image>:tag`

Running the above command will not have any output in the terminal as it just creates the docker container, runs any commands it needs to and destroys itself.

We can add flags to the command in any order to modify this behaviour for our use.

#### Flags

- `-it`: makes the container interactive so that we get the terminal of the container
- `--rm`: deletes the container automatically when stopped
-  `--name <name>`: give the container your own chosen name
- `-v <absolute/path/of/host/directory>:<path/of/directory/in/container>`: mount a directory from host to the container to access from both
- `-net=<network-name>`: to connect it to a network
- `-e <ENVIRONMENT_VARIABLE>=<Value>`: pass an environemnt variable to the container
    - `-e DISPLAY=novnc:0.0`: to connect display of container to noVNC
- `--network=host`: share the networking with the host
- `--ipc=host`: share the shared memory with  the host

## Common Commands

Run a container with display as X11 display manager:
```bash
#Have an X11 display manager open
xhost +

docker run -e DISPLAY=host.docker.internal:0.0 -it <image-name>:<tag>
```

Run a container with display as vnc:
```bash
# Create novnc container
docker network create ros
docker pull theasp/novnc:latest
docker run -d --rm --net=ros \
    --env="DISPLAY_WIDTH=3000" \
    --env="DISPLAY_HEIGHT=1800" --env="RUN_XTERM=no" \
    --name=novnc -p=8080:8080 \
    theasp/novnc:latest

# Go to localhost:8080/vnc.html and Connect

docker run --net=ros -e DISPLAY=novnc:0.0 -it <image-name>:<tag>
```
