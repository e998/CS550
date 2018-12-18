count = 0

while count<5:
	print("hi!")
	count += 1


# utilizing while loops instead of recursion
"""
def question():
	response = input("Give me info!")
	while response != "hi" and response != "b":
		print("This is useless info! Try again.")
		response = input("Give me info!")
	if response == "hi":
		print("a")
	elif response == "b":
		print("b")

question()
"""


"""
def num():
	number = float(input("Pick a number between 1 and 5"))
	while number>5 or number<1:
			print("Error! Not in range.")
			number = input("Pick a number between 1 and 5")
	while number != 
num()
"""


while True:
	try: #######
		num = int(input("Pick a number between 1 and 5: "))
		if 1<=num<=5:
			break
		else:
			print("That's not in the right range.")
	except ValueError:
		print("That's not a number. Try again.")
print("Success!")










