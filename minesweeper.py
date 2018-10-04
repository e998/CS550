# Minesweeper! Step 1
# 10/9/2018

"""
Sources:
- 2-dimensional list - https://stackoverflow.com/questions/22584652/python-how-to-print-out-a-2d-list-that-is-formatted-into-a-grid
"""

import sys
import random as r

w = None
h = None
B = None

def startGame():
	global w,h,B

	print("\n\n\n#################\n" +
		"Play Minesweeper!\n" +
		"#################\n")

	# set dimensions for board
	w = int(sys.argv[1]) + 2
	h = int(sys.argv[2]) + 2
	B = int(sys.argv[3])

	initBoard = [['X']*w for b in range(h)]
	# print user board
	for i in range(1,h-1):
		for j in range(1,w-1):
			# board[i][j]
			print(initBoard[i][j], end=" ")
		sys.stdout.write("\n")


def endGame():
	print("Sorry, you lost!")


def msGame():

	# initial number of adjacent bombs set equal to 0
	board = [[0 for a in range(w)] for b in range(h)]

	# place bombs
	for i in range(B):
		b = r.randint(1,w-2)
		a = r.randint(1,h-2)
		if board[a][b] is not "*": # if not already a bomb
			board[a][b] = "*"
			# determining number of bombs adjacent to selected square
			for i in range(-1,2):
				for j in range(-1,2):
					if board[a+j][b+i] != "*":
						board[a+j][b+i] += 1


	user = input("\nSelect position x,y: ")

	""" code for revealing user position in progress
	if board[a][b] != 'X':
		if board[a][b] == '*':
			endGame()
		else:
			initBoard[a][b] = board[a][b]
	"""

	# print full board
	# len(board)-1 is height
	for i in range(1,len(board)-1):
		# len(board[0])-1 is width
		for j in range(1,len(board[0])-1):
			board[i][j]
			print(board[i][j], end=" ")
		sys.stdout.write("\n")

startGame()
msGame()




