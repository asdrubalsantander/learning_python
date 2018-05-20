#! /usr/bin/env python
# 20-element-search.png
# 
# Write a function that takes an ordered list of numbers (a list where the elements are in order from
# smallest to largest) and another number. The function decides whether or not the given number is
# inside the list and returns (then prints) an appropriate boolean.

from random import randint
import textwrap


def number_exists(numbers, number):
    return True if number in numbers else False


def main():
    numbers = sorted(list({randint(0, 100) for _ in range(0, randint(0, 100))}))
    number = int(input("Insert a number from 0 to 100 to test if exist inside the List \n Number:"))

    print("Is number " + str(number) + " is inside the list?")
    print(textwrap.fill(str(numbers), 70))
    print("Response: " + str(number_exists(numbers, number)) + "!")


if __name__ == '__main__':
    main()
