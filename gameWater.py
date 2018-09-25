# code for the user to choose to go to the water 


# Imports
import random as r
import gameCastle as c
import gameKayak as k


# leaving water section, go to castle or kayaking now
def movefromWater():
	moveWater = input("You decide that you want to do something else now! Do you want to:\n" +
			"1. Make sand castles!\n" +
			"2. Go kayaking!\n\n")
	if moveWater == "1":
		c.sandCastle()
	elif moveWater == "2":
		k.kayak()
	else:
		print("\nYou can't do that! Pick option 1 or 2.\n")


# previous: continueWater()
# user learns about three species of pinnipeds
def seeAnimals():
	print("These lumps seem to be alive! What are these creatures?")
	print("We can figure out what they are by looking at their features. They look like some species of marine mammal!\n")
	w_animal = input("Do they have:\n" +
		"1. Long, funky, elephantesqe noses but no ear flaps?\n" +
		"2. Cute spots that give them a pattern like granite? Are they GALUMPHING???\n" +
		"3. Earflaps? Can they stand up on their foreflippers?\n\n")
	if w_animal == "1":
		print("\nThis is the one and only ELEPHANT SEAL, my friend! You are one lucky duck to get to see them today. " + 
			"Northern elephant seals are grayish and tan in color and only come onshore to mate, give birth, and shed their fur. Males and females are very different in size and appearance. Female elephant seals reach up to 600 kg. Males can grow up to 2,000 kg, and they develop a large nose that looks like an elephant's trunk!\n")
		movefromWater()
	elif w_animal == "2":
		print("\nThis is the PACIFIC HARBOR SEAL, which is one of the most BEAUTIFUL AND ADORABLE animals you will ever meet! LUCKY YOU! They are, in fact, galumphing, which is how they move on land. So cute! " +
			"Harbor seals are the smallest of California pinnipeds, with spotted fur and colorization that varies from white to dark brown. They tend to stay near the shore, in subtidal and intertidal zones, and can often be seen on floating docks or sheltered beaches. Their range within California extends along the entire coast of the state. " +
			"Why is it on the east coast and not in Calfornia right now? This is truly strange and does not happen naturally. The world may never know why you are seeing it today.\n")
		movefromWater()
	elif w_animal == "3":
		print("\nThis is the CALIFORNIA SEA LION!!! SO MAJESTIC AND AMAZING! " +
			"California sea lions have brown fur, act playful, like to stay together in large groups, and sound like barking dogs. You can often see them hauled out on offshore rocks or floating together in large groups called 'rafts'. Males can weigh up to 360 kg, while females may weigh up to 100 kg. " + 
			"Why is it on the east coast and not in Calfornia right now? This is truly strange and does not happen naturally. The world may never know why you are seeing it today.\n")
		movefromWater()
	else:
		print("That's not a choice! Pick option 1, 2, or 3.\n")
		seeAnimals()


# previous: seePlastic()
def pickupPlastic():
	plastic = input("What do you do with the plastic now?\n" +
		"1. Leave it! What can you do?\n" +
		"2. PICK IT UP! Animals could eat it!!!!\n" +
		"3. Play with it! It looks like fun!!\n\n")
	if plastic == "1":
		print("\nWRONG!!! TRY AGAIN!\n\n")
		pickupPlastic()
	elif plastic == "2":
		print("\nYes! You should use gloves to pick the plastic pieces up, but don't just leave it!\n")
		movefromWater()
	elif plastic == "3":
		print("\nWRONG!!! THAT'S DANGEROUS! TRY AGAIN!\n\n")
		pickupPlastic()
	else:
		print("\nThat's not a choice! Pick option 1, 2, or 3!\n")


# previous: continueWater()
def seePlastic():
	print("You get closer to the brightly colored rocks, and you can see that these are not rocks at all! They're hard like rocks, though, and look like little pebbles. What could they be?\n" + 
		"\nYou think about it, and then you remember!\n" +
		"\nThe majority of trash pollution in the ocean is composed of PLASTICS! Plastic does not biodegrade, but it photo-degrades from the sun into smaller pieces. Animals often mistake these small pieces for food. 60-80% of marine debris and 90% of floating debris is plastic. Currently, 1 million sea birds and 100,000 marine mammals die annually from ingesting or becoming entangled in plastic.\n")
	pickupPlastic()


# previous: continueWater()
def seeSyringe():
	print("Oh no! You see that the pointy object is a medical syringe. It may have gotten there through a storm drain, or someone may have flushed it down the toilet.\n")
	pickupSyringe = input("Should you pick it up?\n" +
		"1. Yes, of course!\n" +
		"2. NOOOOOOOOOOO!!!!!!\n\n")
	if pickupSyringe == "1":
		print("\nSTOP! That is very dangerous. TRY AGAIN!\n\n")
		seeSyringe()
	elif pickupSyringe == "2":
		print("\nGood idea! Don't pick it up by yourself! You could get hurt. Notify someone else, like a life guard.\n\n")
		movefromWater()


# previous: continueWater()
def seeStranded():
	print("You see that the unmoving heap is a stranded animal!")
	print("We can figure out what the animal is by looking at its features. It looks like some species of marine mammal!\n")
	w_animal = input("Does it have:\n" +
		"1. A long, funky, elephantesqe nose but no ear flaps?\n" +
		"2. Cute spots that gives it a pattern like granite?\n" +
		"3. Earflaps?\n\n")
	if w_animal == "1":
		print("\nThis is an ELEPHANT SEAL!" + 
			"Northern elephant seals are grayish and tan in color and only come onshore to mate, give birth, and shed their fur. Males and females are very different in size and appearance. Female elephant seals reach up to 600 kg. Males can grow up to 2,000 kg, and they develop a large nose that looks like an elephant's trunk! " +
			"Now, call the Mystic Aquarium in CT at (860) 572-5955 with this information to help the animal!\n")
		movefromWater()
	elif w_animal == "2":
		print("\nThis is a PACIFIC HARBOR SEAL!" +
			"Harbor seals are the smallest of California pinnipeds, with spotted fur and colorization that varies from white to dark brown. They tend to stay near the shore, in subtidal and intertidal zones, and can often be seen on floating docks or sheltered beaches. Their range within California extends along the entire coast of the state. " +
			"Why is it on the east coast and not in Calfornia right now? This is truly strange and does not happen naturally. The world may never know why you are seeing it today.\n" +
			"Now, call the Mystic Aquarium in CT at (860) 572-5955 with this information to help the animal!\n")
		movefromWater()
	elif w_animal == "3":
		print("\nThis is the CALIFORNIA SEA LION!!! SO MAJESTIC AND AMAZING! " +
			"California sea lions have brown fur, act playful, like to stay together in large groups, and sound like barking dogs. You can often see them hauled out on offshore rocks or floating together in large groups called 'rafts'. Males can weigh up to 360 kg, while females may weigh up to 100 kg. " + 
			"Why is it on the east coast and not in Calfornia right now? This is truly strange and does not happen naturally. The world may never know why you are seeing it today.\n" +
			"Now, call the Mystic Aquarium in CT at (860) 572-5955 with this information to help the animal!\n")
		movefromWater()
	else:
		print("That's not a choice! Pick option 1, 2, or 3.\n")
		seeAnimals()


# previous: water()
# if there was no rain, user keeps walking to water
def continueWater():
	print("\nThat's wonderful! Keep on walking to the beautiful shoreline. \n" +
		"Remember: it can be dangerous to be close to the ocean after it rains because storm drains take in all of the dirty water that sweeps the streets and dumps it into our sea! The ocean is the most contaminated during the first three days after a rainstorm, so remember not to visit during this time!!\n")
	inWaterList = ["a group of fairly large, slowly moving lumps", "some VERY brightly colored rocks", "a pointy object", "an unidentifiable, UNMOVING heap"]
	seeWater = r.randint(0,3)
	print("As you walk to the edge of the water, you see " + inWaterList[seeWater] + " lying farther down on the beach. You walk closer.\n")
	if seeWater == 0:
		seeAnimals()
	elif seeWater == 1:
		seePlastic()
	elif seeWater == 2:
		seeSyringe()
	else:
		seeStranded()


# previous: water()
# if there was rain, user chooses to stop walking or continue walking
def rainDecision():
	rainChoice = input("\nOh no! It's been raining. Do you: \n" +
		"1. Just keep walking to the water! It's HOT out here. \n" +
		"2. No, stop!\n\n")
	if rainChoice == "1":
		print("\nABORT! ABORT! It can be dangerous to be close to the ocean after it rains because storm drains take in all of the dirty water that sweeps the streets and dumps it into our sea! The ocean is the most contaminated during the first three days after a rainstorm, so remember not to visit during this time!!" +
			"The dirty water has made you SICK! Come back to the beach next time!\n")
		start()
	elif rainChoice == "2":
		leaveRain = input("\nGood idea! It can be dangerous to be close to the ocean after it rains because storm drains take in all of the dirty water that sweeps the streets and dumps it into our sea! The ocean is the most contaminated during the first three days after a rainstorm, so remember not to visit during this time!!\n")
		movefromWater()
	else:
		print("\nWhoops! That's not a possible answer. Pick option 1 or 2!\n")
		rainDecision()


# previous: water()
def hurricane():
	hurricaneList = ["\nHurricane season is not a good time to go to the beach! Go back inside! Start over!", "\nHurricanes are beautiful. Do you really want to be outside, though? Start over!", "\nDon't be at the beach during a hurricane!!! Start over!\n"]
	print(hurricaneList[r.randint(0,2)])
	start()


# previous: water()
def lightning():
	lightthundList = ["\nThis is a questionable decision. Come back next time! Start over!\n", "\nWhat are the chances of getting hit by lightning? LEAVE NOW. Start over!\n", "\nThe thunder is VERY loud. This storm sounds pretty close! Go home for today! Start over!\n"]
	print(lightthundList[r.randint(0,2)])
	start()


# previous: start()
# user decides to go to water and decides if there was rain or no rain
def water():
	waterIntro = input("\nYou've decided to walk towards the water! It is very pretty and blue. Before you reach it though, you have to ask yourself a question. How has the weather been in the past three days?\n" +
		"1. Sunny!\n" +
		"2. Rainy :(\n" + 
		"3. There was a hurricane!\n" +
		"4. I can still hear the lightning and thunder.\n\n")
	if waterIntro == "1":
		continueWater()
	elif waterIntro == "2":
		rainDecision()
	elif waterIntro == "3":
		hurricane()
	elif waterIntro == "4":
		lightning()
	else:
		print("That can't be the weather! Pick option 1, 2, 3, or 4.")
		water()

