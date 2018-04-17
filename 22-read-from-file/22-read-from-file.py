#! /usr/bin/env python
# 22-read-from-file
# 
# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the
# file, and print out the results to the screen. I have a .txt file for you, if you want to use it!


def main():
    file_name = "random-names.txt"
    with open(file_name, "r") as file:
        data = file.read()

    print("In the file '" + file_name + "' they are " + str(data.count("\n") + 1) + " lines.")


if __name__ == '__main__':
    main()
