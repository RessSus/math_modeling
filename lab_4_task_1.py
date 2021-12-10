import numpy as np

a = np.zeros(3)
a[0] = 2
a[1] = 5
a[2] = 8
def task(a):
  b = len(a)
  bb = 0
  for i in range(b):
    bb += a[i]
  print(bb / b) 

task(a) 
  
