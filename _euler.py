# Method: Euler Method
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
def f(x, y):
    return x + y

x0 = 0
y0 = 1
h = 0.1
n = 10

x = x0
y = y0

for i in range(n):
    y = y + h * f(x, y)
    x = x + h
    print("Step", i+1, "x =", round(x,2), "y =", round(y,4))

print("Final value of y:", y)
