from numpy import array, pi, sqrt
from modern_robotics import IKinSpace

"""IKinSpace:
Computes inverse kinematics in the space frame for an open chain robot

:param Slist: The joint screw axes in the space frame when the
              manipulator is at the home position, in the format of a
              matrix with axes as the columns
:param M: The home configuration of the end-effector
:param T: The desired end-effector configuration Tsd
:param thetalist0: An initial guess of joint angles that are close to
                   satisfying Tsd
:param eomg: A small positive tolerance on the end-effector orientation
             error. The returned joint angles must give an end-effector
             orientation error less than eomg
:param ev: A small positive tolerance on the end-effector linear position
           error. The returned joint angles must give an end-effector
           position error less than ev
:return thetalist: Joint angles that achieve T within the specified
                   tolerances,
:return success: A logical value where TRUE means that the function found
                 a solution and FALSE means that it ran through the set
                 number of maximum iterations without finding a solution
                 within the tolerances eomg and ev.
Uses an iterative Newton-Raphson root-finding method.
The maximum number of iterations before the algorithm is terminated has
been hardcoded in as a variable called maxiterations. It is set to 20 at
the start of the function, but can be changed if needed."""

ev = 0.0001
eomg = 0.001
theat_list_0 = array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
T = array([[0, 1, 0, -0.5],
           [0, 0, -1, 0.1],
           [-1, 0, 0, 0.1],
           [0, 0, 0, 1   ]])
w1 = 109 / 1000
w2 = 82 / 1000
l1 = 425 / 1000
l2 = 392 / 1000
h1 = 89 / 1000
h2 = 95 / 1000

# checking if T is outside the workspace:
if sqrt(w1**2 + w2**2 + l1**2 + l2**2 + h1**2 + h2**2) < sqrt(0.5**2 + 2 * 0.1**2):
    print("T is out of range of the end effector")
    exit()


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

tuple1 = IKinSpace(Slist, M, T, theat_list_0, eomg, ev)
theta = tuple1[0]
found_solution = tuple1[1]

print("the result in deg")
for item in theta:
    print((item % 2*pi) * 180 / pi)

print("\nthe result in rad")
for item in theta:
    print((item % 2*pi))

print()
print("was a solution found: ", found_solution)
