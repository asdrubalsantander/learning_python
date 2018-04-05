#Ex8_1
import os
from random import randint

while(True):
	os.system('clear') 

	p1 = int(input("P1: Rock (0) | Papers (1) | Scissors (2)\n"))

	p2 = randint(0,2)

	print("P2: "+ str(p2))

	if( (p1 == 0 and p2 == 2) or (p1 == 1 and p2 == 0) or (p1 == 2 and p2 == 1) ):
		print("P1 WON!")
	elif( (p2 == 0 and p1 == 2) or (p2 == 1 and p1 == 0) or (p2 == 2 and p1 == 1) ):
		print("P2 WON!")
	else:
		print("IT'S A TIE!")
	
	again = int(input("Press any key to play again \n Exit(9) \n"))

	if( again == 9 ):
		break

