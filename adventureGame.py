# Adventure Beach Game!

# previous: water()
# if there was no rain, user keeps walking to water
def continueWater():
	print("\nYou should have no problem! Keep on walking to the beautiful shoreline. \n" +
		"It can be dangerous to be close to the ocean after it rains because storm drains take in all of the dirty water that sweeps the streets and dumps it into our sea! The ocean is the most contaminated during the first three days after a rainstorm, so remember not to visit during this time!!\n")

# previous: water()
# if there was rain, user chooses to stop walking or continue walking
def rainDecision():
	rainChoice = input("\nDo you keep walking to the water anyway? \n" +
		"1. Yes\n" +
		"2. No\n\n")
	if rainChoice == "1":
		print("\nABORT! ABORT! It can be dangerous to be close to the ocean after it rains because storm drains take in all of the dirty water that sweeps the streets and dumps it into our sea! The ocean is the most contaminated during the first three days after a rainstorm, so remember not to visit during this time!!" +
			"The dirty water has made you SICK! Come back to the beach next time!")
		start()
	elif rainChoice == "2":
		leaveRain = input("\nGood idea! It can be dangerous to be close to the ocean after it rains because storm drains take in all of the dirty water that sweeps the streets and dumps it into our sea! The ocean is the most contaminated during the first three days after a rainstorm, so remember not to visit during this time!! " +
			"Would you like to leave the beach? \n" +
			"1. Yes\n" +
			"2. No\n\n")
	else:
		print("\nWhoops! That's not a possible option. Pick 1 or 2!")
		rainDecision()

# previous: start()
# user decides to go to water and decides if there was rain or no rain
def water():
	waterIntro = input("\nThe weather is very nice today, so you've decided to walk towards the water! The water is very pretty and blue. Before you reach it though, you have to ask yourself a question. Did it rain anytime in the past three days?\n" +
		"1. Yes\n" +
		"2. No\n\n")
	if waterIntro == "1":
		rainDecision()
	elif waterIntro == "2":
		continueWater()

# previous: start()
# user decides to make sand castles
def sandCastle():
	print("hi")

# previous: start()
# user decides to go kayaking
def kayak():
	print("hi")

# starting the game
def start():
	choice = input("\n\n\n\n\n\n\nWelcome! You're at the beach, and you're ready to enjoy your day! \n\n\n" +
		"Do you want to start by: \n" +
		"1. Going to the water! Splish Splash \n" +
		"2. Building a sand castle! \n" + 
		"3. Renting a kayak! \n\n")
	if choice == "1":
		water()

	elif choice == "2":
		sandCastle()

	elif choice == "3":
		kayak()

	else:
		print("Oh no! You can't do THAT at the beach. Pick option 1, 2, or 3!")
		start()

start()