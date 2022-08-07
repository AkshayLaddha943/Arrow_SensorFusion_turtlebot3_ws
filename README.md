<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3/blob/main/Arrow.png" align="right" height="200" width="200" alt="header pic"/>
# Arrow_SensorFusion_turtlebot3

This repository encapsulates the ROS workspace containing the necessary packages and program nodes to simulate a simple turtlebot3 and further performing SLAM on turtlebot3 whilst adding noise to wheel odometry sensor motion model and IMU sensor. It also includes the results folder containing images and videos of simulation of turtlebot3 for different situations and a documentation as part of my Internship with Arrow Electronics (eInfochips).

## Pre-requirements

The simulation requires the following libraries and packages to be installed

- [ROS2 (Foxy)](https://docs.ros.org/en/foxy/Installation.html)

- [turtlebot3](https://github.com/ROBOTIS-GIT/turtlebot3)

- [robot_localization](http://docs.ros.org/en/noetic/api/robot_localization/html/index.html)

- [navigation2](https://navigation.ros.org/)

- [Python 3.6.x - Python 3.8.x](https://www.python.org/)


## Cloning the repository

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


## Source the workspace and start up the turtlebot3 environment

```
source ~/Arrow_SensorFusion_turtlebot3_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/Arrow_SensorFusion_turtlebot3_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models/
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py


#Verify the ros2 topic list by running the command and there should be /odom and /imu topic which indicate that both the sensors are active
ros2 topic list

#Confirm if they are publishing (i.e publisher count should be 1)
ros2 topic info /odom
ros2 topic info /imu
```


## Starting up the robot_localization (ekf_filter node)

```
source ~/turtlebot3_robot_localization_ws/install/setup.bash
ros2 launch robot_localization ekf.launch.py

#Verify the ros2 topic list again and there should be an /odometry/filtered topic
ros2 topic list
```


## Plotting a real-time graph of the odometry and filtered odometry output

```
rqt plot -e
```
The '-e' command removes any past data being plotted on the graph.
Once the graph starts up, in the drop-down menu, select the topics you want to plot. For instance, to plot the x-position values of the sensors, type

"odom/pose/pose/position/x"


## Moving the turtlebot3 around in the gazebo world

```
source ~/Arrow_SensorFusion_turtlebot3_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 run turtlebot3_teleop teleop_keyboard
```


## Visualizing the output in Rviz

```
source  ~/Arrow_SensorFusion_turtlebot3_ws/install/setup.bash
rviz2 -d ~/Arrow_SensorFusion_turtlebot3_ws/src/turtlebot3_simulations/turtlebot3_gazebo/rviz/tb3_gazebo_robot_localization.rviz
```
