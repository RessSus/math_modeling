a = int(input())
b = int(input())
if  b != 0:
  if a % b == 0:
    print(f'Делится - частное {a // b}')
  else:
    print(f' Остаток от деления: {a % b} частное {a // b}')
if b == 0:
  print('Знаменатель равен нулю')