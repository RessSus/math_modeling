a = float(input('Введите первый член '))
b = float(input('Введите знаменатель '))
c = int(input('Введите количество членов '))
print(' ')
print(a)
for i in range(1, c):
  print(a*(b**i))
