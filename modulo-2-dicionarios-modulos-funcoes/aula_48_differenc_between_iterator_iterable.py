# count é um iterador sem fim (itertools)
from itertools import count

c1 = count()
r1 = range(10)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')

# Só podemos iterar em objetos que sejam um iterator, e i no caso representa o __next__ do iterator
for i in c1:
    if i >= 100:
        break

    print(i)
print()

print('range')
for i in r1:
    print(i)
