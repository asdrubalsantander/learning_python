#Ex9_1
from random import randint

num = randint(1,9)
count = 0

while(True):
    guess = input("pick a number | 'exit': ")
    if(guess == "exit"):
        break
    elif(not guess.isdigit()):
        print("wrong key")
    elif(int(guess) > num):
       count+=1
       print("too high!")
    elif(int(guess) < num):
        count+=1
        print("too low!")
    elif(int(guess) == num):
        print("YOU GOTTA BOY, in your : " +str(count)+ " time.")
        break
