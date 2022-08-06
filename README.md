<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3/blob/main/Arrow.png" align="right" height="200" width="220" alt="header pic"/>

# Arrow_SensorFusion_turtlebot3

This repository encapsulates the ROS workspace containing the necessary packages and program nodes to simulate a simple turtlebot3 and further performing SLAM on turtlebot3 whilst adding noise to wheel odometry sensor motion model and IMU sensor. It also includes the results folder containing images and videos of simulation of turtlebot3 for different situations and a documentation as part of my Internship with Arrow Electronics (eInfochips).

## Pre-requirements

The simulation requires the following libraries and packages to be installed

- [ROS2 (Foxy)](https://docs.ros.org/en/foxy/Installation.html)

- [turtlebot3](https://github.com/ROBOTIS-GIT/turtlebot3)

- [robot_localization](http://docs.ros.org/en/noetic/api/robot_localization/html/index.html)

- [navigation2](https://navigation.ros.org/)

- [Python 3.6.x - Python 3.8.x](https://www.python.org/)


## Installing and Cloning the repository

```
git clone https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3
cd Arrow_SensorFusion_turtlebot3_ws
```

## Installing required rosdep packages and dependencies

```
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install <package_name>
#To build a specific package only
colcon build --symlink-install --packages-select <name-of-pkg>
```


## Sourcing the workspace and starting up the turtlebot3 environment

```
source ~/Arrow_SensorFusion_turtlebot3_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/Arrow_SensorFusion_turtlebot3_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models/
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```
Verify the ros2 topic list

```
ros2 topic list
```


## Starting up the robot_localization (ekf_filter node)

```
source ~/turtlebot3_robot_localization_ws/install/setup.bash
ros2 launch robot_localization ekf.launch.py
```
