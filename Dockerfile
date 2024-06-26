FROM ros:jazzy

RUN apt-get update && \
    apt-get install -y libusb-1.0-0-dev && \
    apt-get install -y ros-dev-tools && \
    apt-get install -y ros-jazzy-libcurl-vendor && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /root/ros_ws/src && \
    cd /root/ros_ws/src && \
    git clone https://github.com/aussierobots/ublox_dgnss && \
    git clone https://github.com/tilk/rtcm_msgs

WORKDIR /root/ros_ws

RUN . /opt/ros/jazzy/setup.sh && \
    colcon build

ADD launch /root/ros_ws/launch

