# Simulations and Data Project: Ben's Bagelicious Bagel Bae Goals and Bagelnomics Breakthrough
# Due: 1/17/2019

""" Sources:
- Best Types of Bagels Survey - https://www.ranker.com/list/best-types-of-bagels/ranker-food
- Pie Graph - https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py
"""

### IMPORTS
import random
from random import *
import matplotlib.pyplot as plt


##### Ben's Yearly Bagels Simulation

years = 100000
days = 212 # general calculation of days per school year from 2018-2019 Choate Travel Calendar

b = 0 # initial number of bagels

maxBagels = 84800 # (maximum number of bagels a day)*(number of days) = maximum bagels a year
displayBagels = [0 for i in range(maxBagels)]

bagelsDH = 0 # initial bagels from dining hall
bagelsL = 0 # initial bagels from Lanphier Cafe

for y in range(years):
	for i in range(days):
		chooseDay = randint(0,6)
		if chooseDay == 0: # Monday
			bagelsDH += randint(50,150) # first school day, less people at dining hall for breakfast
			bagelsL += randint(20,60) # more people grabbing breakfast in Lanphier instead of dining hall

		elif chooseDay == 1: # Tuesday
			bagelsDH += randint(60,200) # average dining hall breakfast bagel day
			bagelsL += randint(30,100) # school meeting, Lanphier influx

		elif chooseDay == 2: # Wednesday
			bagelsDH += randint(50,200) # early end to school day, more people grabbing bagels for sports
			bagelsL += randint(10,60) # average Lanphier bagel day

		elif chooseDay == 3: # Thursday
			bagelsDH += randint(60,225) # all-school sleep-in, more people at breakfast
			bagelsL += randint(10,60) # average Lanphier bagel day

		elif chooseDay == 4: # Friday
			bagelsDH += randint(60,210) # average dining hall breakfast bagel day
			bagelsL += randint(10,70) # average Lanphier bagel day

		elif chooseDay == 5: # Saturday
			bagelsDH += randint(100,400) # weekend & testing/sports day, influx of people in dining hall for breakfast
			bagelsL += 0 # Lanphier Cafe closed

		else:
			bagelsDH += randint(100,350) # weekend, influx of people in dining hall for breakfast
			bagelsL += 0 # Lanphier Cafe closed

	displayBagels[bagelsDH+bagelsL] += 1 # total bagels that year from dining hall and Lanphier Cafe

	bagelsDH,bagelsL = 0,0 # reset number of bagels after each year

plt.plot(displayBagels)
plt.xlabel("Number of Bagels Consumed in One Year")
plt.ylabel("Frequency of Annual Number of Consumed Bagels")
plt.title("Ben's Yearly Bagels\n")
plt.show()



##### Ben's Best Bagelicious Bagels Data Pie (Bagel) Graph
# Pie chart

labels = 'Everything','Cinnamon Raisin','Plain','Asiago','Sesame','Blueberry','Onion','Cheddar','French Toast','Poppyseed','Egg','Garlic','Chocolate Chip','Salt','Whole Wheat','Pumpkin'

upvotes = [443,326,323,296,278,277,253,227,215,192,191,180,158,147,132,102]

sizes = [[upvotes[i]/3740] for i in range(16)]
explode = (0.4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3)  # only "explode" Everything Bagels

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.0f%%',
        shadow=True, startangle=0)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

plt.title("Ben's Best Bagelicious Bagels\n")
plt.show()


