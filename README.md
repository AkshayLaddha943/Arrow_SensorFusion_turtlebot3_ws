<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3/blob/main/Arrow.png" align="right" height="200" width="200" alt="header pic"/>

# Arrow_SensorFusion_turtlebot3

This repository encapsulates the ROS workspace containing the necessary packages and program nodes to simulate a simple turtlebot3 and further performing SLAM on turtlebot3 whilst adding noise to wheel odometry sensor motion model and IMU sensor. It also includes the results folder containing images and videos of simulation of turtlebot3 for different situations and a documentation as part of my Internship with Arrow Electronics (eInfochips).

## Pre-requisites

The simulation requires the following libraries and packages to be installed

- [MATLAB R2022a](https://www.mathworks.com/help/control/index.html?s_tid=CRUX_lftnav)

- [Python 3.6.x - Python 3.8.x](https://www.python.org/)


# Multi-D Kalman Filter

<p align="left"> <img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/multi-d%20kalman%20filter/mult-d-kalman_1.PNG" width="400"> 
<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/multi-d%20kalman%20filter/multi-d_kalman_2.PNG" width="425">

Source code: [Notebook](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/Kalman_Filter_python/Multi-D%20Kalman.ipynb)


# Extended Kalman Filter-Python3

<p align="left"> <img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/EKF_results/ekf_1.PNG" width="235" hspace="10"> 
<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/EKF_results/ekf_2.PNG" width="245" hspace="10">
<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/EKF_results/ekf_3.PNG" width="245">

Source code: [Notebook](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/Kalman_Filter_python/EKF.ipynb)



# Extended Kalman Filter-MATLAB (R2022a)

<p align="left"> <img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/EKF_results/ekf_1.PNG" width="235" hspace="10"> 
<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/EKF_results/ekf_2.PNG" width="245" hspace="10">
<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/EKF_results/ekf_3.PNG" width="245">

Source code: [Notebook](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/Kalman_Filter_python/EKF.ipynb)
<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3/blob/main/results/turtlebot3/turtlebot3_gazebo.png" width="480" alt="turtlebot3_simulation">
