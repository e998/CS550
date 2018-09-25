# code for the user to choose to go kayaking


# Imports
import random as r
import gameWater as w
import gameCastle as c


# leaving kayaking section, go to water or castle now
def movefromKayak():
	moveKayak = input("You decide that you want to do something else now! Do you want to:\n" +
			"1. Go to the water!\n" +
			"2. Make sand castles!\n\n")
	if moveKayak == "1":
		w.water()
	elif moveKayak == "2":
		c.sandCastle()
	else:
		print("\nYou can't do that! Pick option 1 or 2.\n")
		movefromKayak()


# previous: kayak()
def continueKayak():
	print("\nThat's wonderful! Go ahead and start kayaking. \n" +
		"Remember: it can be dangerous to be close to the ocean water after it rains because storm drains take in all of the dirty water that sweeps the streets and dumps it into our sea! The ocean is the most contaminated during the first three days after a rainstorm, so remember not to visit during this time!!\n")
	print("That was fun!")
	movefromKayak()


# previous: kayak()
# if there was rain, user chooses to kayak or not kayak
def rainDecision():
	rainChoice = input("\nOh no! It's been raining. Do you:\n" +
		"1. Just get your boat in the water! It's all good.\n" +
		"2. No, stop!\n\n")
	if rainChoice == "1":
		print("\nABORT! ABORT! It can be dangerous to be close to the ocean after it rains because storm drains take in all of the dirty water that sweeps the streets and dumps it into our sea! The ocean is the most contaminated during the first three days after a rainstorm, so remember not to visit during this time!!" +
			"The dirty water has made you SICK! Come back to the beach next time!")
		start()
	elif rainChoice == "2":
		print("\nGood idea! It can be dangerous to be close to the ocean after it rains because storm drains take in all of the dirty water that sweeps the streets and dumps it into our sea! The ocean is the most contaminated during the first three days after a rainstorm, so remember not to visit during this time!!\n\n")
		movefromKayak()
	else:
		print("\nWhoops! That's not a possible answer. Pick option 1 or 2!\n")
		rainDecision()


# previous: water()
def hurricane():
	hurricaneList = ["\nHurricane season is not a good time to kayak! Go back inside! Start over!", "\nHurricanes are beautiful. Do you really want to be outside, though? Start over!", "\nDon't be in the water on a small boat during a hurricane!!! Start over!"]
	print(hurricaneList[r.randint(0,2)])
	start()


# previous: water()
def lightning():
	lightthundList = ["\nThis is a questionable decision. Come back next time! Start over!", "\nWhat are the chances of getting hit by lightning? LEAVE NOW. Start over!", "\nThe thunder is VERY loud. This storm sounds pretty close! Go home for today! Start over!"]
	print(lightthundList[r.randint(0,2)])
	start()


# previous: start()
# user decides to go kayaking
def kayak():
	kayakIntro = input("\nYou've decided to go kayaking! The water is very pretty and blue. Before you reach it though, you have to ask yourself a question. How has the weather been in the past three days?\n" +
		"1. Sunny!\n" +
		"2. Rainy :(\n" + 
		"3. There was a hurricane!\n" +
		"4. I can still hear the lightning and thunder. \n\n")
	if kayakIntro == "1":
		continueKayak()
	elif kayakIntro == "2":
		rainDecision()
	elif kayakIntro == "3":
		hurricane()
	elif kayakIntro == "4":
		lightning()
	else:
		print("That can't be the weather! Pick option 1, 2, 3, or 4.")
		kayak()


