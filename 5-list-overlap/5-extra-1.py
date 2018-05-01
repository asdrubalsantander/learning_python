#! /usr/bin/env python
# 5-list-overlap
#
# Randomly generate two lists to test this

from random import randint

a = [randint(0, randint(0, 100)) for i in range(randint(0, randint(0, 100)))]
b = [randint(0, randint(0, 100)) for i in range(randint(0, randint(0, 100)))]

c = [i for i in a if i in b]

a.sort()
b.sort()
c.sort()

print("List 1: " + str(a))
print("List 2: " + str(b))
print("Commons: " + str(c))
