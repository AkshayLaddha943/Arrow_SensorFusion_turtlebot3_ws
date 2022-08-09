<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3/blob/main/Arrow.png" align="right" height="200" width="200" alt="header pic"/>

# Arrow_SensorFusion_turtlebot3

This repository encapsulates the ROS workspace containing the necessary packages and program nodes to simulate a simple turtlebot3 and further performing SLAM on turtlebot3 whilst adding noise to wheel odometry sensor motion model and IMU sensor. It also includes the results folder containing images and videos of simulation of turtlebot3 for different situations and a documentation as part of my Internship with Arrow Electronics (eInfochips).

## Pre-requisites

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
On performing the above commands, the turtlebot3 gazebo window should start in this way -

<p align="center"> <img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/main/results/turtlebot3/turtlebot3_gazebo.png" height="500" width=500" alt="turtlebot3_simulation">




## Starting up the robot_localization (ekf_filter node)

```
source ~/turtlebot3_robot_localization_ws/install/setup.bash
ros2 launch robot_localization ekf.launch.py

#Verify the ros2 topic list again and there should be an /odometry/filtered topic
ros2 topic list
```
After running the EKF launch file of robot_localization package, you should receive a similiar output -

<p align="center"> <img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/main/results/Arrow_ROS_Results/EKF_output.png" height="120" width="950" alt="turtlebot3_rviz">

P.S: Warnings or error may arise if the ekf launch file is initiated before the turtlebot3 rendering takes place



## Plotting a real-time graph of the odometry and filtered odometry output

```
rqt plot -e
```
The '-e' command removes any past data being plotted on the graph.
Once the graph starts up, in the drop-down menu, select the topics you want to plot. For instance, to plot the x-position values of the sensors, type

"odom/pose/pose/position/x"

The following video provides a real-time comparison of actual sensor measurements and filtered sensor measurements whilst moving the turtlebot3 -


https://user-images.githubusercontent.com/62604049/183757844-adfc9237-0178-4419-ae2d-9a2ce7546622.mp4






## Moving the turtlebot3 around in the gazebo world

```
source ~/Arrow_SensorFusion_turtlebot3_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 run turtlebot3_teleop teleop_keyboard
```

The output from odometry and filtered odometry visualized in Rviz while moving the turtlebot3 around in the environment using thr above command -

https://user-images.githubusercontent.com/62604049/183759447-e74582de-6393-4363-8dd6-047269172687.mp4





## Visualizing the output in Rviz

```
source  ~/Arrow_SensorFusion_turtlebot3_ws/install/setup.bash
rviz2 -d ~/Arrow_SensorFusion_turtlebot3_ws/src/turtlebot3_simulations/turtlebot3_gazebo/rviz/tb3_gazebo_robot_localization.rviz
```

After running the rviz command, the rviz window opens up, in the bottom right, click add and select the topics you want to visualize, In this case, we have visualized the /odom topic and /odometry/filtered topics -

<p align="left"> <img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/main/results/Arrow_ROS_Results/Screenshot%20from%202022-08-03%2001-41-46.png" height="300" width="400" alt="turtlebot3_rviz">

<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/main/results/Arrow_ROS_Results/Screenshot%20from%202022-08-03%2001-48-31.png" height="300" width="400" alt="turtlebot3_rviz">


## Adding noise to odometry motion model equation

```
source  ~/Arrow_SensorFusion_turtlebot3_ws/install/setup.bash
ros2 run pypubsub noiseodom

#run the rostopic list to check if the /noisy_odom topic is being published
ros2 topic list

#Further, visualize the rqt graph and plot the noisy_odom topic
rqt_plot /noisy_odom/pose/pose/position
```

On running the python node, a /noisy_odom gets created which can be visualized in rviz2 as below -

The red arrow indicates the clear odometry measurement and the green arrow denotes the distorted and noisy odometry output

https://user-images.githubusercontent.com/62604049/183763104-badd4344-b756-4ff7-afeb-7bfd37a6e7bf.mp4

Based on the visualization, it is evident that the green arrow shows instability and thus is affected by noise




## Adding bias to the IMU sensor of the turtlebot3 -

1. Navigate to the models folder within the turtlebot3_gazebo package and select the .sdf file for turtlebot3 (burger)
2. Within the .sdf file, go the <imu_link> tag of the turtlebot3
3. Inside the tag, include <bias> term within the <linear_acceleration> section
4. Tune the bias values from 0.005 up till 1.5 or 2


After performing the following, run the simulation again and plot a graph for these outputs

The command presents you with a real-time comparison between actual noisy acceleration values from IMU and filtered acceleration values after being passed through EKF -


```
rqt_plot /imu/pose/pose/acceleration/ /accel/filtered/pose/pose/position

```






## Performing SLAM using turtlebot3 with noisy odometry and noisy IMU values

```
#Before starting SLAM, confirm the turtlebot3_cartographer folder within the install folder of the workspace
source  ~/Arrow_SensorFusion_turtlebot3_ws/install/setup.bash
ros2 launch turtlebot3_cartographer cartographer.launch.py

#Run the teleoperation node to move the robot around, until the entire world is mapped
ros2 run turtlebot3_teleop teleop_keyboard

#Once you are fine with the map, save it
ros2 run nav2_map_server map_saver -f ~/map
```

SLAM was performed for three different inputs of odometry sensor, noisy odometry sensor and a filtered odometry sensor (Extended Kalman Filter) - 

A stable and an undistorted map using simple odometry and imu sensor measurments -

<p align="center"> <img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/main/results/Arrow_ROS_Results/odom_slam.png" height="250" width="300" alt="turtlebot3_simulation">

Further, noise and bias term were added to the odometry and IMU data, and were given as an input to the EKF node - 

<p align="center"><img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/main/results/Arrow_ROS_Results/Screenshot%20from%202022-08-04%2022-09-59.png" height="250" width="300" alt="turtlebot3_noisy" hspace="10">
<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/main/results/Arrow_ROS_Results/EKF_odom_SLAM.png" height="250" width="300" alt="turtlebot3_noisy">



## Autonomous Navigation of Turtlebot3 based on EKF output

```
#Before starting the autonomous navigation, confirm if navigation package is correctly installed using this command
sudo apt install ros-foxy-navigation2

#whilst the turtlebot3 is running, start the navigation stack using this command
ros2 launch nav2_bringup tb3_simulation_launch.py
```
Configure the input of the navigation stack (which is currently set to ekf_filtered odometry output) to noisy_odom in the launch file of the navigation stack
The rviz2 screen shows up, go to it, set the initial pose of the robot by clicking the “2D Pose Estimate” on top of the rviz2 screen. Then click on the map in the estimated position where the robot is in the Gazebo environment. Further, set a goal for the robot to move to by clicking “Navigation2 Goal” button and choose a destination. The turtlebot3 will move to the goal destination.

