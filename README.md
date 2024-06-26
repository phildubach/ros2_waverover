# ROS2 demo on Waveshare WAVE ROVER with Raspberry Pi

## Build the docker image

```bash
docker build -t ros2_ubx .
```

## Run the docker image

```bash
docker run -it --rm --privileged -v /dev/bus/usb:/dev/bus/usb ros2_ubx
```

## Launch the ubx_dgnss node

```bash
~/ros_ws# . install/setup.bash
~/ros_ws# ros2 run ublox_dgnss_node ublox_dgnss_node
```

## Launch the ubx_dgnss node with ntrip corrections

Launches the ubx_dgnss and ntrip_client nodes. The ntrip_client node uses
u-blox PointPerfect corrections. corrections by default, but can be configured
using `host`, `port` and `use_https` arguments. See the launch script for
details.

```bash
~/ros_ws# . install/setup.bash
~/ros_ws# cd launch
~/ros_ws/launch# ros2 launch ./ntrip_pp_launch.py username:=<username> \
                                                  password:=<password> \
                                                  mountpoint:=<mountpoint>
```
