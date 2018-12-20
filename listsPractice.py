import random
from fractions import Fraction

"""
saddlelist = [0][0]

print(saddlelist)


saddle = True

l = []

for i in range(5):
	if l[a][b] < l[i][b]
		saddle = False
for j in range(5):
	if l[a][b] > l[a][b]
		saddle = False
"""

""" ******
import random
h = 5
w = 5
# graylist = [[1,2,3,4],[1,2,3,4]]
graylist= [[random.randint(0,255) for i in range(w)] for j in range(h)]
print(graylist)

for i in range(h):
	for j in range(w):
		graylist[i][j] = 255 - graylist[i][j]
print(graylist)
******
"""



"""
numbers = [1,2,3,4,6,1]
maxnum = max(numbers)
numbers.remove(maxnum)
numbers.append(maxnum)
print(numbers)
"""

"""
saddle = True
l = [[1,2,3,4,5],[1,2,3,4,5]]
for i in range(5):
	for a in range(len(l)):
		for b in range(5):
			if l[a][b] < l[i][b]:
				saddle = False
for j in range(5):
	for a in range(len(l)):
		for b in range(5):
			if l[a][b] > l[a][j]:
				saddle = False
"""


"""
l = [[random.randint(1,10) for j in range(5)] for i in range(5)]
saddlenum = 0
for j in range(len(l)):
    for i in range(len(l)):
        saddle = True
        for a in range(len(l)):
            if l[i][a] > l[i][j]:
                saddle = False
            if l[a][j] < l[i][j]:
                saddle = False
        if saddle:
            print(str(i) + "," + str(j))
            saddlenum += 1
if saddlenum == 0:
	print("No saddle points.")
"""


"""
numbers = [1,8,3,5,6,12,7]
for i in range(1,len(numbers)):
    if numbers[i]%3==0 and numbers[i-1]%2==0 and numbers[i+1]%2==1:
        print("position " + str(i) + ": " + str(numbers[i-1]) + ", " + str(numbers[i]) + ", " + str(numbers[i+1]))
"""







l = [[random.randint(1,9) for j in range(9)] for i in range(9)]
print(l)
for a in range(9):
	if l[a][0] != l[a][1] != l[a][2] != l[a][3] != l[a][4] != l[a][5] != l[a][6] != l[a][7] != l[a][8]:
		row = True
for b in range(9):
	if l[0][b] != l[1][b] != l[2][b] != l[3][b] != l[4][b] != l[5][b] != l[6][b] != l[7][b] != l[8][b]:
		column = True
if row and column:
	valid = True
print(valid)


"""
for a in range(len(l)):
	for b in range(len(l)):
		if str(1) in l[a][b]:
			print(1)
"""
# for i in range(len(l)):











