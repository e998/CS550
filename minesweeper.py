# Minesweeper Game!
# 10/9/2018

"""
Sources:
- 2-dimensional list - https://stackoverflow.com/questions/22584652/python-how-to-print-out-a-2d-list-that-is-formatted-into-a-grid
- String Split - https://www.w3schools.com/python/ref_string_split.asp
- Break - https://www.tutorialspoint.com/python/python_break_statement.htm
"""

import sys
import random as r

w = None
h = None
B = None
initBoard = None

def startGame():
	global w,h,B,initBoard

	print("\n\n\n#################\n" +
		"Play Minesweeper!\n" +
		"#################\n")

	# set dimensions for board
	w = int(sys.argv[1]) + 2
	h = int(sys.argv[2]) + 2
	B = int(sys.argv[3])

	initBoard = [['X']*w for b in range(h)]
	# print userboard
	for i in range(1,h-1):
		for j in range(1,w-1):
			# board[i][j]
			print(initBoard[i][j], end=" ")
		sys.stdout.write("\n")


def endGame():
	print("Sorry, you lost!")


def msGame():
	isPlaying = True

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

	while (isPlaying): 
		user = input("\nSelect position x,y: ")
		position = user.split(",")
		
		# code for revealing user position in progress
		#if board[a][b] != 'X':
		if board[int(position[1])][int(position[0])] == '*':
			initBoard[int(position[1])][int(position[0])] = board[a][b]
			isPlaying = False
			endGame()

		else:
			initBoard[int(position[1])][int(position[0])] = board[int(position[1])][int(position[0])]
			if board[int(position[1])][int(position[0])] == 0:
	
				zero = True
				# down
				d = int(position[1])
				while d <= h-1: 
					if (board[d][int(position[0])] == 0):
						initBoard[d][int(position[0])] = board[d][int(position[0])]
						d += 1
					else:
						break
				
				# up
				u = int(position[1])
				while u >= 0: 
					if (board[u][int(position[0])] == 0):
						initBoard[u][int(position[0])] = board[u][int(position[0])]
						u -= 1
					else:
						break

				# left
				l = int(position[0])
				while l >= 0: 
					if (board[int(position[1])][l] == 0):
						initBoard[int(position[1])][l] = board[int(position[1])][l]
						l -= 1
					else:
						break
				
				# right
				ri = int(position[0])
				while ri <= w-1: 
					if (board[int(position[1])][ri] == 0):
						initBoard[int(position[1])][ri] = board[int(position[1])][ri]
						ri += 1
					else:
						break


		for i in range(1,len(board)-1):
			# len(board[0])-1 is width
			for j in range(1,len(board[0])-1):
				print(initBoard[i][j], end=" ")
			sys.stdout.write("\n")
	
	
"""
	# print full board
	# len(board)-1 is height
	for i in range(1,len(board)-1):
		# len(board[0])-1 is width
		for j in range(1,len(board[0])-1):
			board[i][j]
			print(board[i][j], end=" ")
		sys.stdout.write("\n")
"""


startGame()
msGame()




