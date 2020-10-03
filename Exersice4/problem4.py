from modern_robotics import FKinBody, FKinSpace
import numpy as np
from numpy import array, pi
from sympy import symbols
#  import problem2 as p2
from problem2 import print_array as p2

#  h1, h2, w1, w2, l1, l2 = symbols('h1 h2 w1 w2 l1 l2')
theta = array([0, -pi/2, -pi/2, 0, 0, 0])

w1 = 109
w2 = 82
l1 = 425
l2 = 392
h1 = 89
h2 = 95

M = array([[-1, 0, 0, l1+l2],
          [0, 0, 1, w1+w2],
          [0, 1, 0, h1-h2],
          [0, 0, 0, 1]])

Slist = array([[0, 0, 1, 0, 0, 0],
              [0, 1, 0, -h1, 0, 0],
              [0, 1, 0, -h1, 0, l1],
              [0, 1, 0, -h1, 0, l1+l2],
              [0, 0, -1, -w1, l1+l2, 0],
              [0, 1, 0, h2-h1, 0, l1+l2]]).T

Blist = array([[0, 1, 0, (w1+w2), 0, -(l1+l2)],
              [0, 0, 1, h2, -l1-l2, 0],
              [0, 0, 1, h2, -l2, 0],
              [0, 0, 1, h2, 0, 0],
              [0, -1, 0, -w2, 0, 0],
              [0, 0, 1, 0, 0, 0]]).T

T6space = FKinSpace(M, Slist, theta)
T6body = FKinBody(M, Blist, theta)

#  def print_array(arr):

#      num_rows, num_cols = np.shape(arr)
#      for i in range(num_rows):

#              print(f'{arr[i, 0]} \t\t\t {arr[i, 1]} \t\t\t {arr[i, 2]} \t\t\t {arr[i, 3]}')

#      print(f"\n")

print("T6space")
p2(T6space)
print("T6body")
p2(T6body)

p2(T6space-T6body)
