#! /usr/bin/env python
# 9-extra-1
#
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


from random import randint

num = randint(1, 9)
count = 0

while True:
    guess = input("Pick a number | Or type 'exit' to finish: ")
    if guess == "exit":
        break
    elif not guess.isdigit():
        print("wrong key")
    elif int(guess) > num:
        count += 1
        print("too high!")
    elif int(guess) < num:
        count += 1
        print("too low!")
    elif int(guess) == num:
        count += 1
        print("YOU GOTTA BOY, in your : " + str(count) + " time.")
        break
