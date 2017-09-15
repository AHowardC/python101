#guessNum
import random

comGuess = random.randint(0,100)

while True:
	userGuess = input("Guess a number between 0 - 100:")
	if userGuess > comGuess:
		print("Guess lower")
	elif userGuess < comGuess:
		print("Guess higher")
	else:
		print("Congrats, you got it")
		break  

