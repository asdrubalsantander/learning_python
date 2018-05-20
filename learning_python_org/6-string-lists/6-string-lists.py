#! /usr/bin/env python
# 6-string-lists
# 
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is
# a string that reads the same forwards and backwards.)

phrase = input("Insert a string to test if it's a palindrome: \n")
phrase = phrase.replace(" ", "").lower()
print(phrase[::-1])
print(phrase)

if phrase == phrase[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
