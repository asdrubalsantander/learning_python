#! /usr/bin/env python
# 9-extra-1
#
# Keep the game going until the user types “exit”


from random import randint

num = randint(1, 9)

while True:
    guess = input("Pick a number | Or type 'exit' to finish: ")
    if guess == "exit":
        break
    elif not guess.isdigit():
        print("wrong key")
    elif int(guess) > num:
        print("too high!")
    elif int(guess) < num:
        print("too low!")
    elif int(guess) == num:
        print("YOU GOTTA BOY")
        break
