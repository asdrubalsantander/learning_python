#! /usr/bin/env python
# 2-extra-1
#
# If the number is a multiple of 4, print out a different message.

number = int(input("Hit me! \n"))
if (number % 4) == 0:
    print("EVEN4")
elif (number % 2) == 0:
    print("EVEN")
else:
    print("ODD")
