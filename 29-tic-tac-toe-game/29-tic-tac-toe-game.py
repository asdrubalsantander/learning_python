#! /usr/bin/env python
# 29-tic-tac-toe-game
# 
# This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1,
# Part 2, and Part 3.
# The next step is to put all these three components together to make a two-player Tic Tac Toe game!
# Your challenge in this exercise is to use the functions from those previous exercises all together
# in the same program to make a two-player game that you can play with a friend.
# There are a lot of choices you will have to make when completing this exercise,
# so you can go as far or as little as you want with it.
#
# Here are a few things to keep in mind:
#
# You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
# If there are no more moves left, don’t ask for the next player’s move!
# As a bonus, you can ask the players if they want to play again and keep a running tally of
# who won more - Player 1 or Player 2.

import os


# From exercise 24
def draw_board(game):
    for i in range(3):
        print(" ---" * 3)
        print("|", end="")
        for j in range(3):
            print(" {0} |".format(game[i][j]), end="")
        print()
    print(" ---" * 3)


# From exercise 26
def check_equality(board_list):
    if 0 in board_list:
        return False
    return board_list[1:] == board_list[:-1]


def columns_to_rows(game):
    return [[row[i] for row in game] for i in range(len(game))]


def get_descending_diagonal(game):
    diagonal = []
    for i, row in enumerate(game):
        for j, column in enumerate(game):
            if i == j:
                diagonal.append(row[i])

    return diagonal


def get_rising_diagonal(game):
    rising_diagonal = []
    for i, row in enumerate(game):
        for j, _ in enumerate(game):
            if (i + j) == len(row) - 1:
                rising_diagonal.append(row[j])

    return rising_diagonal


def check_winner(game):
    winner = False

    # check rows for winner
    for i, row in enumerate(game):
        winner = check_equality(row)

        if winner:
            player_winner = row[0]
            print("Player {0}, winner in row: {1}".format(player_winner, i + 1))
            break

    # check columns for winner
    if not winner:
        columns = columns_to_rows(game)
        for i, column in enumerate(columns):
            winner = check_equality(column)

            if winner:
                player_winner = column[0]
                print("Player {0}, winner in column: {1}".format(player_winner, i + 1))
                break

    # check descending diagonal for winner
    if not winner:
        descending_diagonal = get_descending_diagonal(game)
        winner = check_equality(descending_diagonal)

        if winner:
            player_winner = descending_diagonal[0]
            print("Player {0}, winner in descending diagonal".format(player_winner))

    # check rising diagonal for winner
    if not winner:
        rising_diagonal = get_rising_diagonal(game)
        winner = check_equality(rising_diagonal)

        if winner:
            player_winner = rising_diagonal[0]
            print("Player {0}, winner in rising diagonal".format(player_winner))

    return winner


# From exercise 27
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
        draw_board(game)
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
            draw_board(game)
            print("Thanks for play.")
            break

        draw_player_play(game, current_player)
        if check_winner(game):
            break
        current_player = 1 if current_player == 2 else 2


if __name__ == '__main__':
    main()
