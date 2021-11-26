import numpy as np
from lab_3_task_1 import g
xn = int(input())
yn = int(input())
vn = int(input())
wtf = np.zeros((6, 3))
for t in range(0, 6):
  x = xn + vn * t
  y = yn + vn * t - (g * t**2) / 2
  wtf[t, 0] = t
  wtf[t, 1] = x
  wtf[t, 2] = y
print(wtf)