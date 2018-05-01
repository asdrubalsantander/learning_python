#! /usr/bin/env python
#
# 14-list-remove-duplicates
# Write a program that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.


def no_duplicate(numbers):
    return [j for i, j in enumerate(numbers) if j not in numbers[i+1:]]


def main():
    numbers = [2, 1, 12, 3, 123, 123, 12, 3, 412, 3, 12, 3, 123, 123, 1, 132, 124]
    print("List: ", numbers)
    print("List with no duplicates: ", no_duplicate(numbers))


if __name__ == "__main__":
    main()
