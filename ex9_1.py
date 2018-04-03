#Ex9_1
from random import randint

num = randint(1,9)

while(True):
    guess = input("pick a number | 'exit': ")
    if(guess == "exit"):
        break
    elif(not guess.isdigit()):
        print("wrong key")
    elif(int(guess) > num):
        print("too high!")
    elif(int(guess) < num):
        print("too low!")
    elif(int(guess) == num):
        print("YOU GOTTA BOY")
        break
