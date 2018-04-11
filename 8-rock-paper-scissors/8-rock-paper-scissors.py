#! /usr/bin/env python
# 8-rock-paper-scissors
# 
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new
# game)


import os

while True:
    os.system('clear')

    p1 = int(input("P1: Rock (0) | Papers (1) | Scissors (2)\n"))

    p2 = int(input("P2: Rock (0) | Papers (1) | Scissors (2)\n"))

    if (p1 == 0 and p2 == 2) or (p1 == 1 and p2 == 0) or (p1 == 2 and p2 == 1):
        print("P1 WON!")
    elif (p2 == 0 and p1 == 2) or (p2 == 1 and p1 == 0) or (p2 == 2 and p1 == 1):
        print("P2 WON!")
    else:
        print("IT'S A TIE!")

    if (int(input("Insert any number to play again (0-8) | Exit(9) \n"))) == 9:
        break
