#! /usr/bin/env python
# 23-file-overlap
# 
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One
# .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy
# numbers up to 1000.


def main():

    with open("happynumbers.txt","r") as happy_numbers_file, open("primenumbers.txt","r") as prime_numbers_file:
        happy_numbers = [int(i) for i in happy_numbers_file]
        prime_numbers = [int(i) for i in prime_numbers_file]

    print([i for i in happy_numbers if i in prime_numbers])


if __name__ == '__main__':
    main()
