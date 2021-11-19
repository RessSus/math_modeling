import numpy as np

a = [1, 5, 3, 6]

b = a[0:2:1] #0 - нач элемент( пропускается ), 2 - конечный, 1 - шаг

print(b)

c = a[3:0:-1]

print(c)

d = a[::-1]

print(d)

ab = np.array([a, np.array(a) * 3])

print(ab)

n = b[::, 1]
print(n)

m = b[1,2:3:1]
print(m)