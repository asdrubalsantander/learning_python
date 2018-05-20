#! /usr/bin/env python
# 30-pick-word
# 
# This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and
# Part 3.
# In this exercise, the task is to write a function that picks a random word from a list of words from the
# SOWPODS dictionary. Download this file and save it in the same directory as your Python code.
# This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments.
# Each line in the file contains a single word.

from random import randint
import linecache
import os


def get_file_count(path_file):
    return int(os.popen('wc -l < {0}'.format(path_file)).read())


def main():
    path_file = "sowpods.txt"
    num_lines = get_file_count(path_file)
    print("From the file \"{1}\" with {0} lines.".format(num_lines, path_file))
    num_random = randint(1, num_lines)
    print("Reading the line number: {0}".format(num_random))
    print(linecache.getline(path_file, num_random))


if __name__ == '__main__':
    main()
