# 1/8/2019
# CS550 Class Winter

import collections
from collections import *

import random
from random import *

# heads = Counter([])

heads = [0]*11

trials = 10000
for i in range(trials):
	r = 0
	for j in range(10):
		r += randint(0,1)
	heads[r] += 1

print(heads)




