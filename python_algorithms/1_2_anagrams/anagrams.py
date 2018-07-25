#! /usr/bin/env python
#
# 1-2. Find a way of checking whether two strings are anagrams of each other (such as "debit card" and "bad credit").
# How well do you think your solution scales? Can you think of a naïve solution that will scale poorly?

import sys


def main():
    string_1 = sys.argv[1].lower()
    string_2 = sys.argv[2].lower()

    if sorted(string_1) == sorted(string_2):
        print("The first word {} and the second word {} are anagrams!".format(string_1, string_2))
    else:
        print("This two words are not anagrams.")


if __name__ == '__main__':
    main()
