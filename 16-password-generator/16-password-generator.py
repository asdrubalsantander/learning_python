#! /usr/bin/env python
# 16-password-generator
# 
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords
# have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be
# random, generating a new password every time the user asks for a new password. Include your run-time
# code in a main method.

from random import randint
import string


def generate_new_password():
    length = randint(8, 65)
    password = []

    print("length :" + str(length))

    for i in range(0, length + 1):
        password.append(chr(randint(33, 126)))

    return password


def main():
    print("New password generated")
    print("".join(generate_new_password()))


if __name__ == "__main__":
    main()
