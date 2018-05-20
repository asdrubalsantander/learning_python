#! /usr/bin/env python
# 4-divisors
# 
# Create a program that asks the user for a number and then prints out a list of all the divisors of
# that number. (If you don’t know what a divisor is, it is a number that divides evenly into another
# number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Hit me! \n"))
final_list = [i for i in range(num, 0, -1) if (num % i) == 0]
print(final_list)

