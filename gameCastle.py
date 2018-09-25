# code for the user to choose to make sand castles and be in the sand


# Imports
import random as r
import gameWater as w
import gameKayak as k


# leaving sand castle section, go to water or kayaking now
def movefromCastle():
	moveCastle = input("You decide that you want to do something else now! Do you want to:\n" +
			"1. Go to the water!\n" +
			"2. Go kayaking!\n\n")
	if moveCastle == "1":
		w.water()
	elif moveCastle == "2":
		k.kayak()
	else:
		print("\nYou can't do that! Pick option 1 or 2.\n")
		movefromCastle()


# previous: sandCastle()
def sandSyringe():
	print("Oh no! The medical syringe may have gotten there through a storm drain, or someone may have flushed it down the toilet.\n")
	pickupSyringe = input("Should you pick it up?\n" +
		"1. Yes, of course!\n" +
		"2. NOOOOOOOOOOO!!!!!!\n\n")
	if pickupSyringe == "1":
		print("\nSTOP! That is very dangerous. TRY AGAIN!\n\n")
		sandSyringe()
	elif pickupSyringe == "2":
		print("\nGood idea! Don't pick it up by yourself! You could get hurt. Notify someone else, like a life guard.\n\n")
		movefromCastle()
	else:
		print("\nYou can't do that! Pick option 1 or 2.\n")
		sandSyringe()


# previous: sandCastle()
def sandPlastic():
	print("You see that it looks like a brightly colored rock. But these are not rocks at all! It's hard like a rock, though, and it looks like a little pebble. What could it be?\n" + 
		"\nYou think about it, and then you remember!\n" +
		"\nThe majority of trash pollution in the ocean is composed of PLASTICS! Plastic does not biodegrade, but it photo-degrades from the sun into smaller pieces. Animals often mistake these small pieces for food. 60-80% of marine debris and 90% of floating debris is plastic. Currently, 1 million sea birds and 100,000 marine mammals die annually from ingesting or becoming entangled in plastic.\n")
	w.pickupPlastic()


# previous: start()
# user decides to make sand castles
def sandCastle():
	print("You've decided to play in the sand and make sand castles!\n")
	sandList = ["medical syringe", "piece of plastic"]
	sandItem = r.randint(0,1)
	print("This is wonderful! You are having lots of fun. It's a beautiful day!")
	print("Suddenly, you feel a sharp pain in your foot! OW! It's a " + sandList[sandItem] + " hidden in the sand!\n")
	if sandItem == 0:
		sandSyringe()
	elif sandItem == 1:
		sandPlastic()


