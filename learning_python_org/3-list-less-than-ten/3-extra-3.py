#! /usr/bin/env python
# 3-extra-3
#
# Ask the user for a number and return a list that contains only elements from the
# original list a that are smaller than that number given by the user.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
num = int(input("Number: "))
for i in a:
    if i < num:
        b.append(i)

print(a)
print("Smaller than " + str(num))
print(b)
