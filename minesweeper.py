# Minesweeper! Step 1
# 10/2/2018

"""
Sources:
- https://stackoverflow.com/questions/22584652/python-how-to-print-out-a-2d-list-that-is-formatted-into-a-grid
"""

import sys
import random as r

""" earlier edits
w = int(sys.argv[1])
h = int(sys.argv[2])
b = int(sys.argv[3])

board = [[0 for x in range(h)] for x in range(w)]
for i in range(w):
    for j in range(h):
    	 board[i][j] = '%s,%s'%(i,j)
print(board)
"""



w = int(sys.argv[1]) + 2
h = int(sys.argv[2]) + 2
B = int(sys.argv[3])

board = [[0 for a in range(w)] for b in range(h)]

# place bombs
for k in range(B):
	b = r.randint(1,w-2)
	a = r.randint(1,h-2)
	if board[a][b] is not "*":
		board[a][b] = "*"
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

# print board
for i in range(1,h-1):
	for j in range(1,w-1):
		board[i][j]
		print(board[i][j],end=" ")
	sys.stdout.write("\n")



"""
if a>=0 and a<=w and b>=0 and b<=h:
	print ("*")
"""



"""
if board[x-1][y] is not "*":
	board[x-1][y] += 1
	board[x-1][y-1] += 1
"""




