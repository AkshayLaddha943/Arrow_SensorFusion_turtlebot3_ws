# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 19:25:09 2022

@author: acer
"""

pip install numpy --upgrade

import numpy as np
import matplotlib.pyplot as plt
from math import *

#gaussian function
def gauss(mu, sigma2, x):
    coeff = 1.0/ sqrt(2.0 * pi * sigma2)
    expon = exp(-0.5 * (x-mu) ** 2 / sigma2)
    return (coeff * expon)

#update function
def update(m1, v1, m2, v2):
    new_mean = (v2*m1 + v1*m2)/(v2+v1)
    new_var = 1/(1/var2 + 1/var1)
    
    return [new_mean, new_var]

#predict function
def predict(m1,v1, m2, v2):
    new_mean = m1 + m2
    new_var = v1 + v2    
    return [new_mean, new_var]


#measurement and motion
measurement = [5., 6., 7., 8., 9.]
motion = [1., 1., 2., 1., 1.]
measure_uncertain = 4
motion_uncertain = 2
mu = 0
var = 10000


for i in range(len(measurement)):
    #measurment update with uncertainty
    mu, var = update(mu, var, measurement[i], measure_uncertain)
    print('Update: [{}, {}]'.format(mu, var))
    #motion update with uncertainty
    mu, var = predict(mu, var, motion[i], motion_uncertain)
    print('Predict: [{}, {}]'.format(mu,var))
    
    print('Final result: [{}, {}]'.format(mu, var))
    
    
mu = mu
sigma2 = var

# define a range of x values
x_axis = np.arange(-20, 20, 0.1)

# create a corresponding list of gaussian values
g = []
for x in x_axis:
    g.append(f(mu, sigma2, x))

# plot the result 
plt.plot(x_axis, g)