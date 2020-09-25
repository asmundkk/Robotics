from ..robotics import rodriguez
from numpy import array, sqrt, pi

omega = 1 / sqrt(5) * array([0, 1, 2])
theta = sqrt(5)
R = rodriguez(omega, theta)

print("Rodrigez \n", R)

p = array([3, 0, 0])
v = R @ p

print("v = \n", v)
