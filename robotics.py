# run command from the Robotteknikk folder or one level above the Robotics folder
# python -m Robotics.Exersice3.find_g
import numpy as np

def omega_skew_matrix(omega):
# returns a skew symmetric matrix from unit rotation axis and angle

    return np.matrix([[0, -omega[2], omega[1]],
                     [omega[2], 0, -omega[0]],
                     [-omega[1], omega[0], 0]])

def rodriguez(omega_hat, theta):
# calculates the rotation matric from the rotation axis and angle

    return np.identity(3) + np.sin(theta)*omega_skew_matrix(omega_hat) + (1-np.cos(theta))*omega_skew_matrix(omega_hat)**2

def g_inverse(theta, omega):
# calculates g_inverse for a given omega and theta

    omega_skew = omega_skew_matrix(omega)
    return 1 / theta * np.identity(3) - 0.5 * omega_skew + (1 / theta - 0.5 / np.tan(theta/2)) * omega_skew @ omega_skew
