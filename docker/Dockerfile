FROM osrf/ros:humble-desktop-full

RUN apt-get update \
    && apt-get install -y \
    nano \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh entrypoint.sh
COPY bashrc ~/.bashrc

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu \
    && pip3 install ultralytics \
    && pip3 install wget

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

ENTRYPOINT [ "/bin/bash", "/entrypoint.sh" ]

CMD ["bash"]