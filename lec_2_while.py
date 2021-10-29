'''
while <peremena> <uslovie>:
ТЕло

<peremena> += на сколько увеличить чтобы избежать зацикливания 
'''

#i = i + 10 и i += 10 полностью одинаковы

i = 5
while i < 15:
  print('i:', i)
  i += 2

