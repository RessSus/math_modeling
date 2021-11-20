import numpy as np
from lec_3_task_1 import g
xn = int(input())
yn = int(input())
vn = int(input())
x = xn + vn * t
y = xn + vn * t - (g * t**2) / 2
wtf = np.zeros((5, 3))
for t in range(0, 5):
  print(x)