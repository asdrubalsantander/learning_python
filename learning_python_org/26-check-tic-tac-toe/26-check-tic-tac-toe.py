#! /usr/bin/env python
# 26-check-tic-tac-toe
# 
# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1,
# Part 3, and Part 4.
# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly
#  more than half an hour of coding, so we’re doing it in pieces.
#
# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying
# about how the moves were made.
#
# If a game of Tic Tac Toe is represented as a list of lists, like so:
#
# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space,
# and a 2 means that player 2 put their token in that space.
#
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
# tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is
# 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won -
#  assume that in every board there will only be one winner.

from random import randint


def check_equality(board_list):
    if 0 in board_list:
        return False
    return board_list[1:] == board_list[:-1]


def columns_to_rows(board):
    return [[row[i] for row in board] for i in range(len(board))]


def get_descending_diagonal(board):
    diagonal = []
    for i, row in enumerate(board):
        for j, column in enumerate(board):
            if i == j:
                diagonal.append(row[i])

    return diagonal


def get_rising_diagonal(board):
    rising_diagonal = []
    for i, row in enumerate(board):
        for j, _ in enumerate(board):
            if (i + j) == len(row) - 1:
                rising_diagonal.append(row[j])

    return rising_diagonal


def check_winner(board):
    winner = False

    # check rows for winner
    for i, row in enumerate(board):
        winner = check_equality(row)

        if winner:
            player_winner = row[0]
            print("Player {0}, winner in row: {1}".format(player_winner, i + 1))
            break

    # check columns for winner
    if not winner:
        columns = columns_to_rows(board)
        for i, column in enumerate(columns):
            winner = check_equality(column)

            if winner:
                player_winner = column[0]
                print("Player {0}, winner in column: {1}".format(player_winner, i + 1))
                break

    # check descending diagonal for winner
    if not winner:
        descending_diagonal = get_descending_diagonal(board)
        winner = check_equality(descending_diagonal)

        if winner:
            player_winner = descending_diagonal[0]
            print("Player {0}, winner in descending diagonal".format(player_winner))

    # check rising diagonal for winner
    if not winner:
        rising_diagonal = get_rising_diagonal(board)
        winner = check_equality(rising_diagonal)

        if winner:
            player_winner = rising_diagonal[0]
            print("Player {0}, winner in rising diagonal".format(player_winner))

    if not winner:
        print("Not winner found in the current board.")


def main():
    board = [[randint(0, 2), randint(0, 2), randint(0, 2)],
             [randint(0, 2), randint(0, 2), randint(0, 2)],
             [randint(0, 2), randint(0, 2), randint(0, 2)]]

    print("BOARD:")
    for column in board:
        print(column)

    check_winner(board)


if __name__ == '__main__':
    main()
