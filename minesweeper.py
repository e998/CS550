# Minesweeper! Step 1
# 10/9/2018

"""
Sources:
- 2-dimensional list - https://stackoverflow.com/questions/22584652/python-how-to-print-out-a-2d-list-that-is-formatted-into-a-grid
"""

import sys
import random as r

w = int(sys.argv[1]) + 2
h = int(sys.argv[2]) + 2
B = int(sys.argv[3])

board = [[0 for a in range(w)] for b in range(h)]

# place bombs
for i in range(B):
	b = r.randint(1,w-2)
	a = r.randint(1,h-2)
	if board[a][b] is not "*": # if not already a bomb
		board[a][b] = "*"

		"""
		p = [board[a-1][b-1], board[a-1][b], board[a-1][b+1], 
		board[a][b-1], board[a][b+1],
		board[a+1][b-1], board[a+1][b], board[a+1][b+1]]

		for i in range(7):
			if p[i] != "*":
				p[i] += 1
		"""

		if board[a-1][b-1] != "*":
			board[a-1][b-1] += 1
		if board[a-1][b] != "*":
			board[a-1][b] += 1
		if board[a-1][b+1] != "*":
			board[a-1][b+1] += 1

		if board[a][b-1] != "*":
			board[a][b-1] += 1
		if board[a][b+1] != "*":
			board[a][b+1] += 1
		
		if board[a+1][b-1] != "*":
			board[a+1][b-1] += 1
		if board[a+1][b] != "*":
			board[a+1][b] += 1
		if board[a+1][b+1] != "*":
			board[a+1][b+1] += 1
	

""" Hiding items in a list
a = [['A',True], ['B',True], ['C',True], ['D',True], ['E',True]]

def show(index):
    a[index][1] = True

def hide(index):
    a[index][1] = False

def display():
    print([x[0] for x in a if x[1]])
"""


# print initial hidden board
print("\n\n\n#################\n" +
	"Play Minesweeper!\n" +
	"#################\n")

for i in range(1,h-1):
	for j in range(1,w-1):
		board

# print board
for i in range(1,h-1):
	for j in range(1,w-1):
		board[i][j]
		print(board[i][j], end=" ")
	sys.stdout.write("\n")




