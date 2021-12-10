import numpy as np

def taskKR(r):
  S = (r ** 2) * np.pi
  print(S)
  return(S)

def taskKV(kv):
  S = kv ** 2
  print(S)
  return(S)

def taskTR(a, b, c):
  p = (a + b + c) / 2
  S = (p*(p - a) * (p - b) * (p - c)) ** 0.5
  print(S)
  return(S)

print('1 - круг, 2 - квадрат, 3 -треугольник')

ans = int(input())

if ans == 1:
  r = int(input())
  taskKR(r)
elif ans == 2:
  kv = int(input())
  taskKV(kv)
elif ans == 3:
  a = int(input())
  b = int(input())
  c = int(input())
  taskTR(a, b, c)
  