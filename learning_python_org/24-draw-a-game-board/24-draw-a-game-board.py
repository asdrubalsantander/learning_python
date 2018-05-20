#! /usr/bin/env python
# 24-draw-a-game-board
# 
# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.
#
# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
# (8x8 for chess, 19x19 for Go, and many more).
#
# Ask the user what size game board they want to draw, and draw it for them to
# the screen using Python’s print statement.


def draw_board(x, y):

    for i in range(y):
        print(" ---" * x)
        print("|", end="")
        for j in range(x):
            print("   |", end="")
        print()
    print(" ---" * x)


def main():
    print("Let's draw our board:")
    x = int(input("How many rectangles in 'x' axis do you want? \n x:"))
    y = int(input("Now, how many rectangles in 'y' axis do you want? \n y:"))

    draw_board(x,y)


if __name__ == '__main__':
    main()
