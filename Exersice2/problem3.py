import numpy as np
import robotics as rb
from numpy import pi, matrix, array, sqrt, sin, cos

p11 = array([sqrt(2), 0, 2])
p12 = array([0, 2, sqrt(2)])

p21 = array([1, 1, -1])
p22 = array([1/sqrt(2), 1/sqrt(2), -sqrt(2)])

p31 = array([0, 2*sqrt(2), 0])
p32 = array([-sqrt(2), sqrt(2), -2])

def find_rotation_matrix(p1, p2):
    p_cross = np.cross(p1, p2)
    #  print("theta =", theta)
    p_cross_unit = p_cross / np.linalg.norm(p_cross)
    print("should be = 1: ", np.linalg.norm(p_cross_unit))
    theta = np.arccos(p1@p2/(np.linalg.norm(p1)*np.linalg.norm(p2)))

    return rb.rodriguez(p_cross_unit, theta)

print("rotation matrix 1: \n", find_rotation_matrix(p11, p12))
print("rotation matrix 2: \n", find_rotation_matrix(p21, p22))
print("rotation matrix 3: \n", find_rotation_matrix(p31, p32))
