#! /usr/bin/env python
# 36-birthday-plots
# 
# This exercise is Part 4 of 4 of the birthday data exercise series. The other exercises are: Part 1,
# Part 2, and Part 3.
# In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.
#
# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!
# Because it would take a long time for you to input the months of various scientists, you can use my scientist
# birthday JSON file. Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or
# its solution) and draw your histogram.


from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Range1d
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

    x = list(count_months.keys())
    y = list(count_months.values())

    source = ColumnDataSource(dict(x=[calendar.month_name[i] for i in range(1, 13)]))

    output_file("bars.html")
    p = figure(title='Amount of Birthdays of Scientists by Months', plot_width=800, plot_height=400,
               x_range=source.data["x"], y_range=Range1d(0, 3))
    p.vbar(x, width=0.5, bottom=0, top=y, color="firebrick")

    p.yaxis[0].axis_label = "Birthdays"

    show(p)


if __name__ == '__main__':
    main()
