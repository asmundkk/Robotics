from modern_robotics import FKinBody, FKinSpace
import numpy as np
from numpy import array, pi, zeros

theta = array([0, pi/2, -pi/2, 1])
L0 = 1
L1 = 1
L2 = 1

M = array([[1, 0, 0, 0],
          [0, 1, 0, L1+L2],
          [0, 0, 1, L0],
          [0, 0, 0, 1]])

Slist = array([[0, 0, 1, 0, 0, 0],
              [0, 0, 1, L1, 0, 0],
              [0, 0, 1, L1+L2, 0, 0],
              [0, 0, 0, 0, 0, 1]]).T

Blist = array([[0, 0, 1, -(L1+L2), 0, 0],
              [0, 0, 1, -L2, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 1]]).T

T4space = FKinSpace(M, Slist, theta)
T4body = FKinBody(M, Blist, theta)

# this is  not correct i think
Tbs = array([[1, 0, 0, 0],
             [0, 1, 0,-2],
             [0, 0, 1,-1],
             [0, 0, 0, 1]])

def print_array(arr):

    num_rows, num_cols = np.shape(arr)
    for i in range(num_rows):

            print(f'{arr[i, 0]:2.2f} \t {arr[i, 1]:2.2f} \t {arr[i, 2]:2.2f} \t {arr[i, 3]:2.2f}')

    print(f"\n")

print("T4space")
print_array(T4space)
print("T4body")
print_array(T4body)
