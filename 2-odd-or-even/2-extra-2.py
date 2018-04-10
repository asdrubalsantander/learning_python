#! /usr/bin/env python
# 2-extra-2
#
# Ask the user for two numbers: one number to check (call it num) and one number to divide
# by (check). If check divides evenly into num, tell that to the user. If not,
# print a different appropriate message.

number = int(input("Hit me 1! \n"))
check = int(input("Hit me 2! \n"))
if (number%check) == 0:
    print("Just in the target")
else:
    print("Not even close")