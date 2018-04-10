#! /usr/bin/env python
# 1-extra-1
#
# Add on to the previous program by asking the user for another number and
# printing out that many copies of the previous message.

import datetime

now = datetime.datetime.now()
name = input("Hello, how it's your name?")
age = int(input(name + ", and your age is?"))
message = 'The year will be: ' + str(((100 - age) + now.year)) + ' in your 100 year!'
copies = int(input("How many copies do you want? : "))
for i in range(copies):
    print(message)

print((message + "\n") * copies)