# 1/11/2019
# CS550 Class Winter
# Guesstimate: Dessert Calories

### Imports
import random
from random import *

import matplotlib.pyplot as plt


partySeasons = 1000000
display = [0]*40000 # maximum calories per party season is 40000 (10*8*500)
totalCal = 0

for i in range(partySeasons):
	parties = randint(1,10) # 1-10 parties per party season
	for i in range(parties):
		desserts = randint(1,8) # 1-8 desserts per party
		for i in range(desserts):
			calories = randint(40,500) # 40-500 calories per dessert

			totalCal += calories

	# print(totalCal)

	display[totalCal] += 1

	totalCal = 0 # reset number of total calories after each party season

# print(display)


x_axis = [x for x in range(40000)]

# x-axis for bar graph must be included
plt.bar(x_axis, display, color=(0.5, 0.0, 0.5, 1.0))

# plt.plot(x_axis, display)

plt.show()


