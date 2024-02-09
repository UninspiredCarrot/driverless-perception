FROM osrf/ros:humble-desktop-full

ENV DISPLAY novnc:0.0

RUN apt-get update \
    && apt-get install -y \
    nano \
    python3-pip

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu \
    && pip3 install ultralytics \
    && pip3 install wget

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc