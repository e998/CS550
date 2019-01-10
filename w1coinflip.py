# 1/8/2019 - coin flip code
# 1/10/2019 - plotting points
# CS550 Class Winter
# Coin Flip Result Distribution

# Counter (import collections)

import random
from random import *

import matplotlib.pyplot as plt

display = [0]*11

trials = 10000
for i in range(trials):
	r = 0
	for j in range(10):
		r += randint(0,1)
	display[r] += 1

# print(heads)

x_axis = [x for x in range(11)]
data2 = [y for y in range(5,16)]

# there is a default for x-axis of plot
# plt.plot(x_axis, display, 'r*', x_axis, data2, 'b^') # r--, g^, bs

# x-axis for bar graph must be included
plt.bar(x_axis, display, color=(0.5, 0.0, 0.5, 1.0))

plt.xlabel("Number of Heads")
plt.ylabel("Number of Successful Trials")

plt.show()


