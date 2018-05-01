#! /usr/bin/env python
# 15-reverse-word-order
# 
# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#
#   My name is Michele
# Then I would see the string:
#
#   Michele is name My
# shown back to me.


def reversed_phrase(phrase):
    return ' '.join(phrase.split()[::-1])


def main():
    phrase = input("Give me a phrase to reverse it: ")
    print(phrase + ' <-> ' + reversed_phrase(phrase))


if __name__ == "__main__":
    main()
