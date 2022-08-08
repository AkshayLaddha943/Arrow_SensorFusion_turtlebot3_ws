<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3/blob/main/Arrow.png" align="right" height="200" width="200" alt="header pic"/>

# Arrow_SensorFusion_turtlebot3

This branch of the repository presents the simulations associated with Mulit-dimensional Kalman Filter and Extended Kalman Filter using Python3 and MATLAB. Moreover, This branch also includes a results folder containing results for different algorithms and a source code of these algorithms in Jupyter and MATLAB.

## Pre-requisites

The simulation requires the following libraries and packages to be installed

- [MATLAB R2022a](https://www.mathworks.com/help/control/index.html?s_tid=CRUX_lftnav)

- [Python 3.6.x - Python 3.8.x](https://www.python.org/)


# Multi-D Kalman Filter

The following graphs indicate the implementation of Multi-D Kalman Filter for two different cases of minimal noise and an highly noisy motion model equation 

<p align="left"> <img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/multi-d%20kalman%20filter/mult-d-kalman_1.PNG" width="400" span class="image-caption" Kalman Filter with minimal noise> 
<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/multi-d%20kalman%20filter/multi-d_kalman_2.PNG" width="425">

Source code: [Notebook](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/Kalman_Filter_python/Multi-D%20Kalman.ipynb)


# Extended Kalman Filter-Python3


An implementation of EKF below indicates a comparison between state space model values which seem to be underpredicted and EKF values which blends the estimated state value with the sensor data to create a better state estimate of true observations

<p align="left"> <img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/EKF_results/ekf_1.PNG" width="235" hspace="10"> 
<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/EKF_results/ekf_2.PNG" width="245" hspace="10">
<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/EKF_results/ekf_3.PNG" width="245">

Source code: [Notebook](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/Kalman_Filter_python/EKF.ipynb)


# Extended Kalman Filter-MATLAB (R2022a)

An implementation of EKF indicate the implementation of Multi-D Kalman Filter for two different cases of no noise and noise scenario

<p align="left"> <img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/kalman%20filter%20matlab_results/kalman_matlab.PNG" width="235" hspace="10">
<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/kalman%20filter%20matlab_results/kalman_matlab_highsensornoise.PNG" width="245" hspace="10">
<img src="https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/blob/second/results/kalman%20filter%20matlab_results/kalman_matlab_process_noise.PNG" width="245">

Source code: [Notebook](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws/tree/second/Kalman_filter_MATLAB_code)
