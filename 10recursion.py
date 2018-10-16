# 10/9/2018
# Recursion!

"""
1! = 1 = 1 	: base case 

pattern:
2! = 2 = 2*1 = 2*1!
3! = 6 = 3*2*1 = 3*2!
...
n! = n(n-1)!
"""


"""recursive factorial function
# limit to recursive function ~ 998,999
def fact(n):
	# pseudo code - putting function on hold to come back later
	if n is 1:
		# return ends function
		return 1
	return n*fact(n-1)

print (fact(999))
"""


"""
def add(a,b):
	return a+b
"""


#--------------
# Coding Bat!
#--------------

"""counting number of x's in a string with RECURSION!
def countx(user):
	# count = 0
	if len(user) == 0:
		return 0
	elif user[0] == 'x':
		return 1 + countx(user[1:])
	elif user[0] != 'x':
		return countx(user[1:])

user = input("Input string: ")

print("Number of x's:", countx(user))
"""


def crazy_eights(numbers):
	if len(numbers) == 0:
		return 0
	elif numbers[0] == '8':
		if len(numbers) == 1:
			return 1
		elif numbers[1] == '8':
			return 2 + crazy_eights(numbers[1:])
		elif numbers[1] != '8':
			return 1 + crazy_eights(numbers[1:])
	elif numbers[0] != '8':
		return crazy_eights(numbers[1:])

print(crazy_eights("980234024"))









