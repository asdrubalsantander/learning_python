#! /usr/bin/env python
# 35-birthday-months
# 
# This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are: Part 1,
# Part 2, and Part 4.
# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise,
# load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have
# a birthday in each month.
#
# Your program should output something like:
#
# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }


import json
import calendar


def read_birthdays(file):
    with open(file, "r") as data:
        birthdays = json.load(data)
    return birthdays


def count_all_months(birthdays):
    count_ordered_birthdays = {}
    for month in range(1, 13):
        for name in birthdays:
            number_current_month = int(birthdays[name].split("/")[1])
            name_current_month = calendar.month_name[number_current_month]
            if number_current_month == month:
                if name_current_month in count_ordered_birthdays:
                    count_ordered_birthdays[name_current_month] += 1
                else:
                    count_ordered_birthdays[name_current_month] = 1
    return count_ordered_birthdays


def main():
    file = "birthdays.json"
    birthdays = read_birthdays(file)
    count_months = count_all_months(birthdays)
    print(count_months)


if __name__ == '__main__':
    main()