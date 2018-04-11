#! /usr/bin/env python
# 9-guessing-game-one
# 
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then
# tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user
# input lessons from the very first exercise)

from random import randint

num = randint(1, 10)
guess = int(input("pick a number: "))

if guess > num:
    print("too high!")
elif guess < num:
    print("too low!")
else:
    print("YOU GOTTA BOY")
