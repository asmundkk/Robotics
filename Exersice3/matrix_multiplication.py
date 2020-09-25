from sympy import symbols, cos, sin
from numpy import array

a, b, c = symbols('a, b, c')

R12 = array([[1, 0, 0], [0, cos(a), -sin(a)], [0, -sin(a), cos(a)]])
R23 = array([[cos(b), 0, sin(b)], [0, 1, 0], [-sin(b), 0, cos(b)]])
R34 = array([[cos(c), -sin(c), 0], [sin(c), cos(c), 0], [0, 0, 1]])

print("R12 \n")
print(R12, "\n")

print("R23 \n")
print(R23, "\n")

print("R34 \n")
print(R34, "\n")

print("R04 = \n")
print(R34@R23@R12)

print("R04 = \n")
print(R12@R23@R34)

print("B: \n")
print(R34@R12@R23)
