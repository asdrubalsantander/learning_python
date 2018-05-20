#! /usr/bin/env python
# 31-guess-letters
# 
# This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and
# Part 3.
# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player
#  has to guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed.
# (In the actual game, the player can only guess 6 letters incorrectly before losing).
#
# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player
#  to guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess
#  an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed
#  and display a different message if the player tries to guess that letter again. Remember to stop the game when all
# the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number
# of guesses the player has remaining - we will deal with those in a future exercise.


def introduction(user_findings):
    print("Welcome to the Hangman Game!")
    print("Give a try to guess the secret word")
    print(user_findings)


def ask_letters(secret_word, user_findings, user_used_letters):
    while True:
        if '_' not in user_findings:
            print("Congratulations you have found the secret word: {0}".format(secret_word))
            break
        print("Remember you have use the following letters {0}".format(sorted(list(user_used_letters))))
        user_letter = input("User find the word with one letter at the time: ").lower()
        if len(user_letter) == 1:
            user_used_letters.add(user_letter)
            for i, letter in enumerate(secret_word):
                if user_letter == secret_word[i]:
                    user_findings[i] = letter
            print(user_findings)
        else:
            print("Only input one letter, please.")


def main():
    secret_word = "secret"
    user_findings = ["_" for _ in secret_word]
    user_used_letters = set()

    introduction(user_findings)

    ask_letters(secret_word, user_findings, user_used_letters)


if __name__ == '__main__':
    main()
