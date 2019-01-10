# 1/10/2019
# CS550 Class/HW Winter

import random
from random import *

import math
from math import *

# home coordinates
x = 0
y = 0

trips = 1000
blocks = 10

forwardback = [1.0, -1.0] # person moves forward one, back one, up one, or down one for each step

walk = 0

for i in range(trips):
	for j in range(blocks):
		moveXorY = randint(0,1) # person moves along x-axis or y-axis
		if moveXorY == 0:
			x += choice(forwardback)
		elif moveXorY == 1:
			y += choice(forwardback)

	if abs(x) + abs(y) <= 4:
		print(x,y)
		print(abs(x) + abs(y))
		walk += 1

	# reset x and y coordinates after each trip
	x = 0
	y = 0

print(str(walk) + "/" + str(trips)) # result: about 80% of the time (800/1000)






