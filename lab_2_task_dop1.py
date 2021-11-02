a = int(input())
b = int(input())
c = int(input())
D = (b ** 2) - (4 * a * c)
e = D ** 0.5
if D == 0:
  x = -b / (2 * a)
  print(x)
elif D < 0:
  print('Нет корней')
else:
  x = (-b + e) / (a * 2)
  y = (-b - e) / (a * 2)
  print(x, y)