a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
  if a == b or b == c or a == c:
    print('Треугольник существует; он равнобедренный')
  elif a == b == c:
    print('Треугольник существует; он равносторонний')
  else:
    print('Треугольник существует; он разносторонний')
else:
  print('Треугольник не существует')