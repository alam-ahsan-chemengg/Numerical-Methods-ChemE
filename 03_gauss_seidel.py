# Method: Gauss Seidel Method
# Subject: Numerical Methods in Chemical Engineering
# Author: Ahsan Alam
import numpy as np

A = np.array([[4,1,2],
              [3,5,1],
              [1,1,3]], dtype=float)

B = np.array([4,7,3], dtype=float)

x = np.zeros(len(B))

for it in range(10):
    for i in range(len(B)):
        s = 0
        for j in range(len(B)):
            if j != i:
                s += A[i][j] * x[j]
        x[i] = (B[i] - s) / A[i][i]
    print("Iteration", it+1, ":", x)

print("Final solution:", x)
