# 9/18/2018

def hi():
	print("Hello!")

hi()


def start():
	choice = input("\n\n\n\n\nGreetings! You are heading to the dining hall one day when there's a bear walking with a dinosaur on campus!! Do you \n\n1) stay inside, or \n walk with them?\n\n>> ")
	if choice == "1":
		inside()

	elif choice == "2":
		walkWithDinoBear()
	else:
		print("Please enter a 1 or a 2. Thank you!")
		start()

def inside():
	choice = input("Lame! You run into Lanphier for shelter in place. But you get really thirsty. and you want some water. Do you: 1) go get water? or 2) stay hidden?")
	print("Lame!")
def walkWithDinoBear():
	pass

start()
# exit() <-- end the entire game