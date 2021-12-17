a = 0
n = 0

def step(a, n):
  a = int(input()) 
  n = int(input()) 
  ax = a 
  for i in range(n-1):
    ax = ax * a
  print(ax)
  return(ax)

step(a, n)
