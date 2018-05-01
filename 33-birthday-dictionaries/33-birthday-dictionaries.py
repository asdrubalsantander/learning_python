#! /usr/bin/env python
# 33-birthday-dictionaries
# 
# This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2,
# Part 3, and Part 4.
# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information
# based on their name. Create a dictionary (in your file) of names and birthdays. When you run
# your program it should ask the user to enter a name, and return the birthday of that person back to them.


def fill_dict():
    birthdays = dict()
    with open("birthdays.txt", "r") as birthday_file:
        for line in birthday_file:
            name, surname, year = tuple(line.split(" "))
            birthdays[name + " " + surname] = year

    return birthdays


def introduction(birthdays):
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    [print(birthday_friend) for birthday_friend in birthdays]


def look_for_birthday(birthdays):
    birthday_friend = input("Who's birthday do you want to look up?\n Birthday Boy/Girl: ")

    if birthday_friend in birthdays:
        print(birthday_friend + "'s birthday is " + birthdays[birthday_friend])


def main():
    birthdays = fill_dict()

    introduction(birthdays)
    look_for_birthday(birthdays)


if __name__ == '__main__':
    main()
