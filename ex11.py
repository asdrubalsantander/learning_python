#Ex11
from math import sqrt

def checkPrime(number):
    return [i for i in range(2,int(sqrt(number))) if number%i==0]

number = int(input("Hit me! \n"))
if len(checkPrime(number)) == 0 and number != 1 and number != 0:
    print("ppppprimebiatch")
else:
    print("NOT PRIME")