def continueWater():
	print("\nYou should have no problem! Keep on walking to the beautiful shoreline. \n" +
		"It can be dangerous to be close to the ocean after it rains because storm drains take in all of the dirty water that sweeps the streets and dumps it into our sea! The ocean is the most contaminated during the first three days after a rainstorm, so remember not to visit during this time!!\n")

# previous: water()
# if there was rain, user chooses to stop walking or continue walking
def rainDecision():
	rainChoice = input("\nOh no! It rained before.  \n" +
		"1. Just keep walking to water! It's HOT out here. \n" +
		"2. No\n\n")
	if rainChoice == "1":
		print("\nABORT! ABORT! It can be dangerous to be close to the ocean after it rains because storm drains take in all of the dirty water that sweeps the streets and dumps it into our sea! The ocean is the most contaminated during the first three days after a rainstorm, so remember not to visit during this time!!" +
			"The dirty water has made you SICK! Come back to the beach next time!")
		start()
	elif rainChoice == "2":
		leaveRain = input("\nGood idea! It can be dangerous to be close to the ocean after it rains because storm drains take in all of the dirty water that sweeps the streets and dumps it into our sea! The ocean is the most contaminated during the first three days after a rainstorm, so remember not to visit during this time!! " +
			"Where should you move instead? \n" +     
			"1. Build a sand castle!\n" +
			"2. Go kayaking!\n\n")
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