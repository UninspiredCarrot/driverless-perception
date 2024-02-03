FROM osrf/ros:galactic-desktop

WORKDIR /eufs_folder

# Update package repositories and install dependencies
RUN apt-get update && apt-get -y upgrade \
    && apt-get -y install python3-pip \
    && pip3 install colcon-common-extensions -U \
    && apt-get -y install ros-galactic-turtle-tf2-py ros-galactic-tf2-tools ros-galactic-tf-transformations

# Clone repositories
RUN git clone https://gitlab.com/eufs/eufs_sim \
    && git clone https://gitlab.com/eufs/eufs_msgs \
    && git clone https://gitlab.com/eufs/eufs_rviz_plugins

# Set environment variable
ENV EUFS_MASTER=/eufs_folder

# Source ROS setup file
RUN /bin/bash -c "source /opt/ros/galactic/setup.sh"

# Update rosdep and install dependencies
RUN rosdep update --include-eol-distros \
    && rosdep install --from-paths $EUFS_MASTER --ignore-src -r -y

# Build packages
RUN /bin/bash -c "colcon build"

# Add ROS setup to .bashrc
RUN echo "source /eufs_folder/install/setup.sh" >> ~/.bashrc

# Set display environment variable for GUI applications
ENV DISPLAY host.docker.internal:0.0
