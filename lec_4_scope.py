x0 = 10 #переменная в глобальной области видимости
def move(t):
  x = x0 * t
  return x0

print(move(3))

#print(x) - ошибка тк х в локальной области функции 

a = 'Good'

def my_func():
  a = 'Bad'
  print(a)

my_func()

print(a)

# int, float, complex   str    tuple - неизменяемые
# list     set     dict - изменяемые

