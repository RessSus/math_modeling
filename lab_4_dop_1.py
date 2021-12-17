a = float(input()) 
n = int(input()) 

def step(a, n):
  ax = a 
  for i in range(n-1):
    ax = ax * a
  print(ax)
  return(ax)

step(a, n)
