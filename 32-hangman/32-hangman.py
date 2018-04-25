#! /usr/bin/env python
# 32-hangman
# 
# This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and
# Part 2.
# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect
#  guesses (head, body, 2 legs, and 2 arms) before they lose the game.
#
# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing
# the letter and displaying that information to the user. In this exercise, we have to put it all together and add
# logic for handling guesses.
#
# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
#
# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize
# them - let them guess again.

from random import randint
import linecache
import os


def get_file_count(path_file):
    return int(os.popen('wc -l < {0}'.format(path_file)).read())


def introduction(user_findings):
    print("Welcome to the Hangman Game!")
    print("Give a try to guess the secret word")
    print(user_findings)


def ask_letters(secret_word, user_findings, user_used_letters):
    number_guesses = 0
    correct_guess = False
    while True:
        # Check if the user has already won
        if '_' not in user_findings:
            print("Congratulations you have found the secret word: {0}".format(secret_word))
            break

        # Check if the user is dead
        if number_guesses >= 6:
            print("Sorry you are dead! The correct word was: {0}".format(secret_word))
            break

        # Print letters already input
        if len(user_used_letters) > 0:
            print("Remember you have use the following letters {0}".format(sorted(list(user_used_letters))))

        # Print lives
        print("You only left {0} {1}".format(6 - number_guesses, "tries" if number_guesses < 4 else "try"))

        user_letter = input("User find the word with one letter at the time: ").lower()
        if len(user_letter) == 1:
            number_guesses += 1
            user_used_letters.add(user_letter)
            for i, letter in enumerate(secret_word):
                if user_letter == secret_word[i]:
                    correct_guess = True
                    user_findings[i] = letter
            print(user_findings)

            if correct_guess or user_letter in user_used_letters:
                number_guesses -= 1
                correct_guess = False
        else:
            print("Only input one letter, please.")


def main():
    path_file = "sowpods.txt"
    num_lines = get_file_count(path_file)
    num_random = randint(1, num_lines)
    secret_word = linecache.getline(path_file, num_random).replace("\n", "").lower()

    user_findings = ["_" for _ in secret_word]
    user_used_letters = set()

    introduction(user_findings)
    ask_letters(secret_word, user_findings, user_used_letters)


if __name__ == '__main__':
    main()
