def changer(a, b):
  a = 2
  b[0] = 'Good'

x = 10
L = [1, 2]

changer(x, L)

print(x)
print(L)

L = [1, 2]

changer(x, L[:]) # СПИСОК ГЛОБАЛЬНО НЕ ИЗМЕНИТСЯ

print(L)
x = 3
y = 4

z = complex(x, y)

print(z)

w = complex(y, x)

print(z + w)

s = 'hello'
print(s[0])

#s[0] = 'H' - ОШИБКА 

t = (1, 4, 9) # картеж - неизменяемый СПИСОК

print(t)
print(t[0])
#t[0] = 3 - ОШИБКА

i = [1, 4, 9]
i[0] = 3
print(i)

d = {'al':4, 4:'al', 'str':'Hello'} # СЛОВАРЬ - вызов по любым ключам

print(d['al'])

print(d[4])
print(d['str'])
d['str'] = 'GOdd'

print(d)