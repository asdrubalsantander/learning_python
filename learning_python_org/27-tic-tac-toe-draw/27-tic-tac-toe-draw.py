#! /usr/bin/env python
# 27-tic-tac-toe-draw
# 
# The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place
# an X on the screen, they can’t just click on a terminal. So we are going to approximate this clicking simply by
# asking the user for a coordinate of where they want to place their piece.
#
# Things to note:
#
# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player)
#  will always be O.
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0).
# To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience
# if the row counts and column counts start at 1. This is not required, but whichever way you choose to implement this,
# it should be explained to the player.
# Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number.
# Then you can use your Python skills to figure out which row and column they want their piece to be in.
# Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game
# position where there already is another piece, do not allow the piece to go there.
# Bonus:
#
# For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full.
#  In a bonus version, keep track of how many squares are full and automatically stop asking for moves
# when there are no more valid moves.

import os


def print_board(game):
    for row in game:
        print(row)


def check_full_board(game):
    full_board = True
    for line in game:
        if 0 in line:
            full_board = False

    return full_board


def draw_player_play(game, player):
    correct_play = False
    while not correct_play:
        os.system('clear')
        print_board(game)
        try:
            player_play_x = int(input("Player {0}, input the x coordinate for your play. \n x:".format(player)))
            player_play_y = int(input("Player {0}, input the y coordinate for your play. \n y:".format(player)))

            if 1 <= player_play_y <= 3 and 1 <= player_play_x <= 3:
                if game[player_play_y - 1][player_play_x - 1] == 0:
                    game[player_play_y - 1][player_play_x - 1] = 'X' if player == 1 else 'O'
                    correct_play = True
                else:
                    print("Another play it's already on that coordinates.")
            else:
                print("Hey don't try to think out of the box!")

        except ValueError:
            print("You can only input numbers")


def main():
    current_player = 1
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    while True:
        if check_full_board(game):
            print_board(game)
            print("Thanks for play.")
            break

        draw_player_play(game, current_player)
        current_player = 1 if current_player == 2 else 2


if __name__ == '__main__':
    main()
