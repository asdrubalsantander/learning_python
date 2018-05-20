#! /usr/bin/env python
# 34-birthday-json
# 
# This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1,
# Part 3, and Part 4.
# In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise,
#  modify your program from Part 1 to load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.
#
# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary,
# and update the JSON file you have on disk with the scientist’s name. If you run the program multiple
# times and keep adding new names, your JSON file should keep getting bigger and bigger.

import json


def read_birthdays(file):
    with open(file, "r") as data:
        birthdays = json.load(data)
    return birthdays


def introduction(birthdays):
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    [print(birthday_friend) for birthday_friend in birthdays]


def look_for_birthday(birthdays):
    birthday_friend = input("Who's birthday do you want to look up?\n Birthday Boy/Girl: ")

    if birthday_friend in birthdays:
        print(birthday_friend + "'s birthday is " + birthdays[birthday_friend])


def user_input_birthday():
    name = input("User please input the name of the new scientist: ")
    birthday = input("Now please input the birthday for {} (format: DD/MM/YYYY) : ".format(name))
    return {name: birthday}


def insert_birthday(file, entry):
    with open(file) as f:
        data = json.load(f)

    data.update(entry)

    with open(file, 'w') as f:
        json.dump(data, f)


def main():
    file_path = "birthdays.json"
    birthdays = read_birthdays(file_path)

    introduction(birthdays)
    look_for_birthday(birthdays)
    entry = user_input_birthday()
    insert_birthday(file_path, entry)


if __name__ == '__main__':
    main()
