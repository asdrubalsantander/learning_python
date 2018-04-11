#! /usr/bin/env python
# 11-check-primality-functions
# 
# Ask the user for a number and determine whether the number is prime or not. (For those who have
# forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer
# to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

from math import sqrt


def check_prime(number):
    return [i for i in range(2, int(sqrt(number))) if number % i == 0]


number = int(input("Write a number to test if it's a prime: \n"))
if len(check_prime(number)) == 0 and number != 1 and number != 0:
    print("It's a prime")
else:
    print("It's not a prime")
