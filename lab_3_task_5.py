import numpy as np
N = 5
M = 4
NxM = np.zeros((N,M))
for i in range(N):
  for j in range(M):
    if i == 0 and j == 0:
      NxM[i, j] = np.sin(N * (i+1) + M * (j + 1))
    else:
      NxM[i, j] = np.sin(N * i + M * j)
    if NxM[i, j] < 0: 
      NxM[i, j] = 0
print(NxM)

for i in range(0, N):
  for j in range(0, M-1):
    NxM[i, j], NxM[i, j+1]  = NxM[i, j+1], NxM[i, j]
print(NxM)

a = np.zeros((2,2))
a[0, 0] = 1
a[0, 1] = 2
a[1, 0] = 3
a[1, 1] = 4
print(a)
for i in range(0, 2):
    a[i, 0], a[i, 1]  = a[i, 1], a[i, 0]
print(a)