#! /usr/bin/env python
# 1-character-input
# 
# Create a program that asks the user to enter their name and their age. Print out a message addressed
# to them that tells them the year that they will turn 100 years old.

import datetime

now = datetime.datetime.now()
name = input("Hello, how it's your name?")
age = int(input(name + ", and your age is?"))
print('The year will be: ' + str(((100 - age) + now.year)) + ' in your 100 year!')
