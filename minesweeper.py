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


def endGame():
	print("\nSorry, you lost! Play again!\n")


"""
def win():
	if the number of unrevealed tiles + number of flags = number of bombs
"""


def flag():	
	position.pop(0)
	x = position[1]
	y = position[0]
	initBoard[int(x)][int(y)] = "F"
	# if user == "F" + str(flagx) + str(flagy):
	print(initBoard[int(x)][int(y)])


def msGame():
	# startGame()
	global w,h,B,initBoard

	print("\n\n\n\n#################\n" +
		"Play Minesweeper!\n" +
		"#################\n")

	######## set dimensions for board
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
	########

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


	# to ensure gutter values are not equal to 0

	# first row of board in gutter, all terms equal to 1 (times the width)
	# brackets around 1 only necessary because done for multiple terms (*w)
	board[0] = [1]*w
	# last row of board in gutter, all terms equal to 1 (times the width)
	board[-1] = [1]*w

	# loop to change values of first gutter column and last gutter column to 1
	# i is row number in board
	# terms of 1D list i is term in row
	for i in board:
		i[0] = 1
		i[-1] = 1


	while (isPlaying): 
		user = input("\nSelect position x y: ")
		global position 
		position = user.split(" ")
		x = position[1]
		y = position[0]

		if position[0] == "F":
			flag()
		else:
		# code for revealing user position in progress
		#if board[a][b] != 'X':
			if board[int(position[1])][int(position[0])] == '*':
				initBoard[int(position[1])][int(position[0])] = board[a][b]
				isPlaying = False
				endGame()

			else:
				initBoard[int(position[1])][int(position[0])] = board[int(position[1])][int(position[0])]
				if board[int(position[1])][int(position[0])] == 0:

					"""
					- while loop, pulling elements out of the zeroes list, list of coordinates
					- tuples - 2D list [[1,2],[3,7],[2,8]]
					"""

					# list of zeroes
					# z is a 2D list!
					z = []
					z.append([ int(position[1]) , int(position[0]) ])


				while len(z) > 0:
					# deleting and returning FIRST term of zeroes list!
					pos = z.pop(0)
					for i in range(-1,2):
						for j in range (-1,2):

							# if the term is equal to zero and it has not been revealed before
							if board[pos[0]+i][pos[1]+j] == 0 and initBoard[pos[0]+i][pos[1]+j] == 'X':
								z.append([pos[0]+i , pos[1]+j])
							initBoard[pos[0]+i][pos[1]+j] = board[pos[0]+i][pos[1]+j]
				sys.stdout.write("\n")


		# printing board
		for i in range(1,len(board)-1):
			# len(board[0])-1 is width
			for j in range(1,len(board[0])-1):
				print(initBoard[i][j], end=" ")
			sys.stdout.write("\n")

	msGame()


msGame()




