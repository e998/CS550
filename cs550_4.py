# 9/14/2018

""" comparisons
if you want opposite result, simply put comparison inside not()
ex. x+y < z is true, but not(x+y < z) is false
"""

# 4 spaces = tab (for indent)


""" Checking only for rain
rain = input("Is it raining outside?" + "\n")

# parentheses not necessary for if-else statements
if(rain == "Yes" or rain == "yes"):
	print("Bring your umbrella!")
else:
	print("You won't need your umbrella, but have a nice day!")
"""


# Weather Options
weather = input("Choose the option for your weather conditions outside: " + "\n"
	"1. Sunny" + "\n"
	"2. Rainy" + "\n"
	"3. Hurricanes" + "\n"
	"4. Lightning and Thunder" + "\n")

if(weather == "1"):
	print("Go outside! Enjoy a day at the beach.")
elif(weather == "2"):
	print("Bring an umbrella!")
elif(weather == "3"):
	print("Find a hurricane shelter!")
else:
	print("Stay safe, don't get hit by lightning!")


