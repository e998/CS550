# Esther Sojung An
# 10/9/2018
# Minesweeper Game!

# On my honor, I have neither given nor received unauthorized aid.

"""
Sources:
- 2-dimensional list - https://stackoverflow.com/questions/22584652/python-how-to-print-out-a-2d-list-that-is-formatted-into-a-grid
- String Split - https://www.w3schools.com/python/ref_string_split.asp
"""


# IMPORTS
import sys
import random as r


w = None
h = None
B = None
initBoard = None


def endGame():
	print("\nSorry, you lost! Play again!\n")


def win():
	# pseudo code - win if the number of unrevealed tiles + number of flags = number of bombs
	print("You win!!! CONGRATULATIONS! Play again!\n")


# counting number of unrevealed tiles
def countX():
	global countx
	countx = 0
	for i in range(1,len(initBoard)-1):
		# len(board[0])-1 is width
		for j in range(1,len(initBoard[0])-1):
			if initBoard[i][j] == 'X':
				countx +=1


# counting number of flags
def countF():
	global countf
	countf = 0
	for i in range(1,len(initBoard)-1):
		# len(board[0])-1 is width
		for j in range(1,len(initBoard[0])-1):
			if initBoard[i][j] == 'F':
				countf +=1


def flag():	
	if initBoard[int(float(position[2]))][int(float(position[1]))] == 'X':
		position.pop(0)
		x = position[1]
		y = position[0]
		initBoard[int(x)][int(y)] = "F"


def msGame():
	global w,h,B,initBoard

	print("\n\n\n\n#################\n" +
		"Play Minesweeper!\n" +
		"#################\n")

	# set dimensions for board
	w = int(sys.argv[1]) + 2
	h = int(sys.argv[2]) + 2
	B = int(sys.argv[3])

	# initBoard is user board
	initBoard = [['X']*w for b in range(h)]

	# print initBoard
	for i in range(1,h-1):
		for j in range(1,w-1):
			# board[i][j]
			print(initBoard[i][j], end=" ")
		sys.stdout.write("\n")

	# boolean if game is playing
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
		# i[-1] is the last term of the list
		i[-1] = 1


	while (isPlaying): 
		user = input("\nSelect position x y: ")
		global position
		# user coordinate input translated to code
		position = user.split(" ")
		x = position[0]
		y = position[1]

		# if user flags a coordinate
		if position[0] == "F":
			flag()
			sys.stdout.write("\n\n")

		# if user reveals a tile
		else:
			# bomb revealed, user loses
			if board[int(y)][int(x)] == '*':
				initBoard[int(y)][int(x)] = board[a][b]
				isPlaying = False
				endGame()

			# numbers revealed, user continues game
			else:
				initBoard[int(y)][int(x)] = board[int(y)][int(x)]
				if board[int(y)][int(x)] == 0:
					# list of zeroes
					# z is a 2D list!
					z = []
					z.append([ int(y) , int(x) ])

				# printing user board throughout game
				while len(z) > 0:
					# deleting and returning FIRST term of zeroes list!
					pos = z.pop(0)
					for i in range(-1,2):
						for j in range (-1,2):

							# if the term is equal to zero and it has not been revealed before, add to z list
							if board[pos[0]+i][pos[1]+j] == 0 and initBoard[pos[0]+i][pos[1]+j] == 'X':
								z.append([pos[0]+i , pos[1]+j])
							initBoard[pos[0]+i][pos[1]+j] = board[pos[0]+i][pos[1]+j]
				sys.stdout.write("\n\n")

				countX()
				countF()
				
				# if sum of unrevealed tiles and flagged tiles equals number of bombs, user wins
				if (countx + countf) == B:
					isPlaying = False
					win()

		# printing board during game
		for i in range(1,len(board)-1):
			# len(board[0])-1 is width
			for j in range(1,len(board[0])-1):
				print(initBoard[i][j], end=" ")
			sys.stdout.write("\n")

	msGame()


msGame()




