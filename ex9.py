#Ex9
from random import randint

num = randint(1,10)
guess = int(input("pick a number: "))

if(guess > num):
    print("too high!")
elif(guess < num):
    print("too low!")
else:
    print("YOU GOTTA BOY")
