#Ex16

from random import randint
import string

def generateNewPassword():
    length = randint(8,65)
    password = []

    print("length :" + str(length))

    for i in range(0,length +1):
        password.append(chr(randint(33,126)))

    return password

def main():
    print("".join(generateNewPassword()))


if __name__ == "__main__":
    main()