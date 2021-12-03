import numpy as np
a = np.zeros((5))
for i in range(4):
  a[i] = int(input())
print(a)
b = int(input('Позиция '))
c = int(input('Значение '))
sus = 5 - (b+1)
for i in range(sus, 0, -1):
  if sus == 1:
    a[4] = c
  else:
    a[b+i] = a[b]
    a[b] = c
print(a)    