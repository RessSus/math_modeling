a = int(input())
b = a
c = 0
for i in range (1, b-1):
   if a % i == 0:
     c = c + i

if b == c:
  print('Число совершенно')
else:
  print('Число несовершенно')