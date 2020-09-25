import numpy as np
from ../robotics import rodriguez

def rotx(theta):
    x = np.array([1, 0, 0])
    return rodriguez(x,theta)

def roty(theta):
    y = np.array([0, 1, 0])
    return rodriguez(y,theta)

def rotz(theta):
    z = np.array([0, 0, 1])
    return rodriguez(z,theta)

print("By inserting the calculated values for omega_hat and theta:\n",
        rodriguez(1/np.sqrt(13)*np.array([2, 0, 3]), np.pi*np.sqrt(13)/12), "\n")

print("Calculating Rab by using rotx and roty:\n", rotx(np.pi/6)*rotz(np.pi/4), "\n")
