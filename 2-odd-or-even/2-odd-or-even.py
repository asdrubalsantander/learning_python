#! /usr/bin/env python
# 2-odd-or-even
# 
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate
# message to the user.

number = int(input("Hit me! \n"))
if (number % 2) == 0:
    print("EVEN")
else:
    print("ODD")
