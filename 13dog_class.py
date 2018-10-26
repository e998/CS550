# 10/25/2018

""" Properties
- breed
- size
- color
- name *
- home
- food/diet
- owner
- tricks 
- energy *
- hunger *
- thirst
- happiness
"""

""" Methods
- walk
- eat *
- sleep *
- play fetch
- roll over
- bark
- bite
- follow owner
- sit
"""

# name with capital letter and with singular
class Seal:

	### CONSTRUCTOR
	# initalizes properties and sets up the dog object

	# self refers to the class
	# though self is passed around, it does not need to be referenced

	# name, hunger, energy - local variables
	def __init__(self, name, hunger, energy, ):
		# scale can be determined (keep in mind, not written down - out of 10)
		self.hunger = hunger
		self.energy = energy
		# self.happiness = happiness
		# names for all dogs not the same
		self.name = name


	### METHODS / FUNCTIONS

	def eat(self, amount):
		status = ""
		if self.hunger > 0:
			# hunger: 0 is full, 10 is very hungry
			self.hunger -= 1
			# energy: 0 is tired, 10 is energetic
			self.energy += amount
			statusEat = self.name + " just ate a delicious meal!"
		else:
			statusEat = self.name + " refused to eat because they are full!"
		return statusEat

	def sleep(self, time):
		status = ""
		if self.energy <= 10-time:
			self.energy += time
			statusSleep = self.name + " just had a wonderful nap!"
		else:
			statusSleep = self.name + " is not tired and doesn't want to sleep!"
		return statusSleep

	def stats(self):
		return "\nName: " + self.name + "\nEnergy: " + str(self.energy) + "\nHunger: " + str(self.hunger)

# want to keep class as flexible as possible, don't ask for input or print things in a class
sealname = input("What do you want to name your seal?\n")
seal1 = Seal(sealname, 5, 2)
seal2 = Seal("Enhy", 3, 9)

while True:
	print(seal1.stats())
	print(seal2.stats())
	choice = input("\n\nWhat do you want to do?\n")
	if choice == "Eat":
		print(seal1.eat(2))
		print(seal2.eat(2))
	elif choice == "Sleep":
		print(seal1.sleep(2))
		print(seal2.sleep(2))
	else:
		print("Your seal can't do that!")




