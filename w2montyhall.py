# 1/8/2019
# CS550 Class/HW Winter

### IMPORTS
import random
from random import *

"""
Before code: Is it better to switch your box or not? Does it matter?
	It is better to switch your box. My instinct is to compare the probability of selecting the 
box with the car key on the first guess to that of selecting a box with pennies on the first guess.
There is a 1/3 chance that you pick the right box at the very beginning, which is why the situation
where the player never switches their box will produce a 1/3 probability of winning. On the other hand, 
there is a 2/3 chance that the player selects the wrong box. If the player has chosen the wrong box and 
is made aware of the other wrong box, it is in their best interest to switch. There is a higher 
probability that the player chooses the wrong box, rather than the right one, on their first guess, 
which corresponds to higher chances of winning if the player chooses to switch boxes.
"""

player = input("Monty Hall Problem: Never switch boxes or always switch boxes?\n" +
	"1. Never\n" +
	"2. Always\n")

trials = 1000
wins = 0

if player == "1": # If the player never switches
	for i in range(trials):
		prize = 1
		choice = randint(1,3)

		if prize == choice:
			wins += 1
	print(str(wins)+"/"+str(trials))

### The player wins the car an average of about 334 out of 1000 times if they never switch.


elif player == "2": # If the player always switches
	for i in range(trials):
		choice = randint(0,2)

		doors = [0]*3

		prize = randint(0,2)
		doors[prize] = 1

		for i in range(3): # showing door without prize
			if doors[i] != 1 and i != choice:
				revealed = i
				break

		for j in range(3): # switching door
			if j != choice and j != revealed:
				choice = j
				break

		if prize == choice:
			wins += 1
	print(str(wins)+"/"+str(trials))

### The player wins the car an average of about 666 out of 1000 times if they always switch.


else:
	print("Rerun simulation.")


"""
Results of simulation:
	The player wins the car with a probability of about 2/3 if they always switch and a probability of
about 1/3 if they never switch. This result was what was expected. Along with the logic mentioned before 
the code was run, the problem can also be understood in the context of more than three boxes. For 
example, if 100 boxes were presented at the very beginning and the player guessed a certain one, they
would have a 1% chance of being right. If the game host revealed 98 boxes that didn't have the car key,
they would leave the same two unknowns: the originally chosen box and one uncovered box. The player is 
much more likely to switch boxes in this case, since the unlikelihood of the player selecting the right 
box on the first try is made much more obvious. They would definitely have a higher probability of 
winning if they decided to change their box. Though the corresponding probabilities in this example are 
different from the that of the original problem, this makes the solution more clear.
"""


