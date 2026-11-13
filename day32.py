import numpy as np
from scipy import linalg

A = np.array([[3,2,-1],[-1,4,2],[1,-1,-3]])
B = np.array([10,8,2])

solution = linalg.solve(A, B)
print("Solution:", solution)

# Verification
print("Verification A @ solution =", A @ solution)
