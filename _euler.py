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
