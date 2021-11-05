a = int(input())
b = a
while a > 1:
  for i in range (2, b+1):
    if a % i == 0:
      print(i, end=' ')
      a = a // i
    if a < 1:
      break
    