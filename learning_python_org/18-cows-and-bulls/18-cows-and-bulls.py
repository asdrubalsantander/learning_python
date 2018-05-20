#! /usr/bin/env python
# 18-cows-and-bulls
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.

from random import randint


def check_user_number(number, user_number):
    list_number = [[i, 0, 0] for i in number]  # list_number = [One Number Random, It's a cow?, It's a Bull?]
    for i, j in enumerate(list_number):
        if user_number[i] == j[0]:
            j[1] = 1  # The current number it's a Cow!
            j[2] = 0  # If it was a Bull not anymore
        else:  # The current number it's not a cow
            for k, l in enumerate(list_number):
                if user_number[i] == l[0] and not l[1] and not l[2]:
                    l[2] = 1  # The current number it's a bull
                    break

    return sum([int(i[1]) for i in list_number]), sum([int(i[2]) for i in list_number])


def main():
    number = str(randint(1000, 10000))
    tries = 0

    while True:
        user_number = input("GuessMe: ")
        c, b = check_user_number(number, user_number)
        print("cows:", c, " bulls:", b)
        tries += 1
        if c == 4:
            print("You found the hidden number: ", number, " with ", tries, " tries.")
            break


if __name__ == "__main__":
    main()
