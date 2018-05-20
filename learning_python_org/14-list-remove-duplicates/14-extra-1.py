#! /usr/bin/env python
# 14-extra-1
#
#  Write two different functions to do this - one using a loop and constructing a list, and another using sets.


def no_duplicates_list(numbers):
    return [j for i, j in enumerate(numbers) if j not in numbers[i+1:]]


def no_duplicates_set(numbers):
    return set(numbers)


def main():
    numbers = [2, 1, 12, 3, 123, 123, 12, 3, 412, 3, 12, 3, 123, 123, 1, 132, 124]
    print("List: ", numbers)
    print("List with no duplicates: ", no_duplicates_list(numbers))
    print("Set with no duplicates: ", no_duplicates_set(numbers))


if __name__ == "__main__":
    main()
