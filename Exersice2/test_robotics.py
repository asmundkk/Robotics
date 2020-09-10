import numpy as np
import robotics as rb

#  print(np.linalg.norm(np.array([3, 4])))

omega = np.array([1, 2, 0])
theta = np.linalg.norm(omega)
omega_hat = omega / theta

print("matrix values: \n", rb.rodriguez(omega_hat,theta))

# lets have have
#  dot_product = np.linalg.dot(omega,omega)
dot_product = omega @ omega
print("the dot product of omega and omega = ", dot_product)
