import numpy as np

a = -4
b = 4
N = 10
def task(a, b, N):
  x = np.linspace(a, b, N)
  y = x**2
  print(y)
  return y
  '''for x in np.arange(a, b + N, N):
    y = x ** 2
    print(y)
    '''

task(a, b, N)