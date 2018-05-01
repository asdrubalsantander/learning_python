#! /usr/bin/env python
# 10-list-overlap-comprehensions
# 
# This week’s exercise is going to be revisiting an old exercise (see Exercise 5),
#  except require the solution in a different way.
#
# Take two lists, say for example these two:
#
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are
# common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#  Write this in one line of Python using at least one list comprehension.


from random import randint

a = {randint(0, randint(0, 100)) for i in range(randint(0, randint(0, 100)))}
b = {randint(0, randint(0, 100)) for i in range(randint(0, randint(0, 100)))}

c = {i for i in a for j in b if i == j}

print("Set of numbers 1: " + str(a))
print("Set of numbers 2: " + str(b))
print("Set of commons numbers: " + str(c))
