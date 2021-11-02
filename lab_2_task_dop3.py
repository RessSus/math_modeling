a = int(input())
b = str()
c = str()
while a > 1:
  c = str(a % 10)
  b = str(b + c)
  a = int(a // 10)
print(b)
