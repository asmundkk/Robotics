from ..robotics import g_inverse
from numpy import array, sqrt, pi

omega = 2 / sqrt(3) * array([1, -1, 1])
theta = 2 / 3 * pi
G = g_inverse(theta, omega)

print("G inverse = \n", G)

p = array([3, 0, 0])
v = G @ p

print("v = \n", v)
