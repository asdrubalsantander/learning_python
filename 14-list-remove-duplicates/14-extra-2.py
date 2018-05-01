#! /usr/bin/env python
# 14-extra-1
#
#  Go back and do Exercise 5 using sets, and write the solution for that in a different function.




def no_duplicates_set(a, b):
    return set(a) | set(b)


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    print("List 1: ", a)
    print("List 2: ", b)
    print("No duplicates with Sets: ", no_duplicates_set(a, b))


if __name__ == "__main__":
    main()
