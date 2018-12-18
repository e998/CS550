# 9/13/2018 

# Currency Converter
# Dollars to Yen

""" Dollars to Yen Conversion
dollars = float(input("Dollars: "))
# print(type(dollars)) - automatically assumes string because user can input anything into command line
# concatenation: ex. x='7', y='4', x+y='74'
yen = dollars * (111.60)
# print("Yen: " + str(yen))
# not concatenation, how it prints out various arguments: comma prints space between arguments
print("Yen:", yen)
"""

# Conversion Calculator
print("Conversion Calculator " + "\n"
	"1. Dollars to Yen" + "\n"
	"2. Miles to Kilometers")
choice = input()
if (choice == "1"):
	dollars = float(input("Dollars: "))
	yen = dollars * (111.60)
	print("Yen:", yen)
elif (choice == "2"):
	mi = float(input("Miles: "))
	km = mi * (1.60934)
	print("Kilometers:", km)


import random
# return the next random floating point number in the range [0.0, 1.0)
# can multiply random.random() by any coefficient to get any range you want
# random.random()


""" print a random number in set: 50, 60, 70, ...,100 with random.randint() 
a = random.randint(5, 10)
x = a * 10
print(str(x))
"""

""" print a random number in set: 50, 60, 70, ...,100 with random.randrange()
print(random.randrange(50, 101, 10))
"""

"""
import math
***
a = math.pow(math.sin(random.random(0, 2*pi), 2) + math.pow(math.cos(, 2)
print(a)
"""


"""
def commandCall(argNum):
	sys.argv[]
	return
"""


# Module: Functions already defined, gives functionality after import











