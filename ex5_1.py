#Ex5
from random import randint

a = [ randint(0, randint(0,100)) for i in range(randint(0,randint(0,100))) ]
b = [ randint(0, randint(0,100)) for i in range(randint(0,randint(0,100))) ]

c = [ i for i in a for j in b if i == j ]
a.sort()
b.sort()
c.sort()
print(a)
print(b)
print(c)