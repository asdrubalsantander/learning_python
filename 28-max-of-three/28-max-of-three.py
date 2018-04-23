#! /usr/bin/env python
# 28-max-of-three
# 
# Implement a function that takes as input three variables, and returns the largest of the three. Do
# this without using the Python max() function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us.
# All you need is some variables and if statements!


def custom_max(value1, value2, value3, ):
    if value1 >= value2 and value1 >= value3:
        return value1

    if value2 >= value1 and value2 >= value3:
        return value2

    if value3 >= value1 and value3 >= value2:
        return value3


def main():
    print('')
    print('Input three values to get the biggest one:')
    value_1 = int(input("value 1: "))
    value_2 = int(input("value 2: "))
    value_3 = int(input("value 3: "))

    print("The biggest value is: {0}".format(custom_max(value_1, value_2, value_3)))


if __name__ == '__main__':
    main()
