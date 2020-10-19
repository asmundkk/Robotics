import numpy as np
from numpy import sin, cos, arccos, arcsin, sqrt, arctan2, pi

L1 = 3
L2 = 2
L3 = 1

thb = 0
xb = 4
yb = 2

th3 = thb

x3 = xb - L3 * cos(th3)
y3 = yb - L3 * sin(th3)

alpha = arccos((L1**2 + L2**2 + x3**2 + y3**2) / (2 * sqrt(xb**2 + yb**2) * L1))
beta = arccos((L1**2 + L2**2 - x3**2 - y3**2) / (2 * L1 * L2))
gamma = arctan2(x3, y3)

# elbow down solution
th1_down = gamma - alpha
th2_down = pi - beta

# elbow up solution
th1_up = gamma + alpha
th2_up = beta - pi

print("elbow down solution")
print("th1", th1_down * 180 / pi)
print("th2", th2_down * 180 / pi)
print("th3", (thb - th1_down -th2_down) * 180 / pi)
print()

print("elbow up solution")
print("th1", th1_up * 180 / pi)
print("th2", th2_up * 180 / pi)
print("th3", (thb - th1_up - th2_up) * 180 / pi)
