# Esther Sojung An
# 9/25/2018
# Adventure Beach Game!

"""
Sources:
- calling functions from another file: (https://stackoverflow.com/questions/20309456/call-a-function-from-another-file-in-python)
- understanding import for files: (https://stackoverflow.com/questions/2349991/how-to-import-other-python-files)
- python lists: (https://www.w3schools.com/python/python_lists.asp)
- marine mammal information: (http://www.marinemammalcenter.org/education/marine-mammal-information/pinnipeds/)
"""

# On my honor, I have neither given nor received unauthorized aid.


# Imports
import gameWater as w
import gameCastle as c
import gameKayak as k


# starting the game
def start():
	choice = input("\n\n\n\n\n\n\nWelcome! You're at the beach, and you're ready to enjoy your day! \n\n\n" +
		"Do you want to start by: \n" +
		"1. Going to the water! Splish Splash! \n" +
		"2. Building a sand castle! \n" + 
		"3. Renting a kayak! \n\n")
	if choice == "1":
		w.water()
	elif choice == "2":
		c.sandCastle()
	elif choice == "3":
		k.kayak()
	else:
		print("Oh no! You can't do THAT at the beach. Pick option 1, 2, or 3!")
		start()


start()


