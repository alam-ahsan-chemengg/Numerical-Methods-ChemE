def f(x):
  return x**3 - x - 1
def df(x):
  return 3*x**2 - 1

x = 1.5
for i in range(10):
  x = x - f(x)/df(x)
  print("Iteration", i+1, "Root =", x)
