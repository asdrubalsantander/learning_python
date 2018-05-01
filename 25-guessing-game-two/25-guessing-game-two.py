#! /usr/bin/env python
# 25-guessing-game-two
# 
# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
#
# At the end of this exchange, your program should print out how many guesses it took to get your number.
#
# As the writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
# But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50
# (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program,
# try to find the optimal strategy

from time import sleep


def introduction():
    print("Lovely user can you think in a number from 1 to 100.")
    sleep(4)
    print("Thanks!")
    sleep(2)
    print("Now, because my name it's 'THE GRAND PYTHONIC', will guess your number.")


def question(number_guessed):
    answer = 'x'
    while answer not in ('y', 'h', 'l'):
        print("It's your number {0}? Or tell me, my guess was too high (press h), or too low (press l), "
              "or I have already guessed it (press y)".format(number_guessed))
        answer = input("answer: ").lower()
        if answer == 'y':
            print("off course it's the right answer because I'm 'THE GRAND PYTHONIC'")
        elif answer in ('h', 'l'):
            print("an error on my calculus. It cant be! You must be lying to me. Because I'm 'THE GRAND PYTHONIC'")
        else:
            print("Don't try to fool me, you mortal!")

    return answer


def guess(pivot, answer, previous_guess):
    pivot = 1 if pivot == 1 else int(pivot / 2)
    if answer == 'l':
        number_guessed = pivot + previous_guess
    else:
        number_guessed = abs(pivot - previous_guess)

    return pivot, number_guessed


def main():
    pivot = 50
    number_guessed = 50

    introduction()
    answer = question(number_guessed)

    while answer != 'y':
        pivot, number_guessed = guess(pivot, answer, number_guessed)
        answer = question(number_guessed)


if __name__ == '__main__':
    main()
