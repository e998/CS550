def moves(n,left):
	if n==0:
		return
	moves(n-1, not left)
	if left:
		print(str(n)+'left')
	else: 
		print(str(n)+'right')
	moves(n-1, not left)

# left is boolean
moves(5, True)