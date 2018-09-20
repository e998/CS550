# 9/18/2018

import random

def numberGame():
	number = random.randint(1,10)
	choice = int(input("\n\n\nPick an integer between 1 and 10.\n"))
	if (choice >= 0 and choice <= 10):
		if (int(choice) == number):
			print("Congratulations! You chose the correct number.")
		elif (int(choice) > number):
			print("Oh no! Your number is too big.")
		else:
			(int(choice) < number);
			print("Oh no! Your number is too small")
	else:
		print("Your input is no good! Type in a number in the range [1,10]")


numberGame()