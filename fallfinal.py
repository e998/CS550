# Esther Sojung An
# 11/14/2018
# Fall Final Project: More Fractals!
# 

# On my honor, I have neither given nor received unauthorized aid.

""" SOURCES:
- Turtle module - https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.radians
- Koch Snowflake pseudo-code - https://scratch.mit.edu/projects/110378199/#editor
"""

### IMPORTS
from math import *  # for koch snowflake and pythagoras tree
import turtle  # for all fractals



### Koch Snowflake Code

# l is initial length of side of triangle
l = 50
# x is original heading
x = 0
# y and z - direction of turtle movement rotates 60˚ forward or 60˚ backwards while drawing snowflake
y = x + 60
z = x - 60

# N is variable used in changing turtle.pencolor while drawing snowflake
N = 0
# turtle.width() - width of line
turtle.width(10)

# turtle.pu() - pull the pen up, no drawing when moving
turtle.pu()
# turtle.goto(x,y) - moving pen location
turtle.goto(-100,-200)
# turtle.pd() - pull the pen down, drawing when moving
turtle.pd()

# innerkoch() - inside first iteration of koch snowflake
# repeats process of dividing sidelength by 3, replacing center section with triangle
def innerkoch(n):
	# n is number of iterations left to do
	global x, y, z, N

	# KOCH SNOWFLAKE OUTLINE COLOR
	# turtle.colormode sets range for color in RGB; chose min. value = 0, max. value = 255
	turtle.colormode(255)
	# turtle.pencolor dependent on changing N value, displays a repeating gradient
	turtle.pencolor( (100*N + 10)%255, N%255, N%255)

	# must begin drawing if n (number of iterations left to do) equals zero
	if n == 0:
		# change N variable to shift turtle.pencolor for gradient
		N += 10
		# actually drawing each line segment, length of line always 1/3 of previous length
		# program does not start drawing until n=0 and this code is reached because must smallest iterations must be drawn first to complete details of the snowflake
		turtle.fd(l/3)

	else:
		# basic illustration of first iteration: _/\_
		# repeats first iteration process for all four line segments in koch curve, for a certain number of iterations

		# turtle.seth = turtle.setheading; heading of turtle set to x, which is 0
		turtle.seth(x)
		# (SEGMENT 1 for koch curve) repeats first iteration: dividing sidelength by 3, replacing center section with triangle for first line segment, before triangle bump
		innerkoch(n-1)

		# rotate x value to -60, redefine x
		x -= 60
		# reset turtle heading to new x
		turtle.seth(x)
		# (SEGMENT 2 for koch curve) repeats first iteration for first side up the triangle
		innerkoch(n-1)

		# rotate x to value to 60 by going forward 120 from -60
		x += 120
		turtle.seth(x)
		# (SEGMENT 3 for koch curve) repeats first iteration for second side down the triangle
		innerkoch(n-1)

		# rotate x to value 0 again by going -60 from 60
		x -= 60
		turtle.seth(x)
		# (SEGMENT 4 for koch curve) repeats first iteration for last line segment of iteration, after triangle bump
		innerkoch(n-1)

# koch() - drawing entirety of snowflake, all three sides of "triangle" that are formed with iterations of the koch curve
def koch(iter):
	global l, x, y, z
	# drawing first side of triangle
	innerkoch(iter)
	# rotate 120 for next side of triangle
	x += 120

	# second side of triangle
	# set heading of turtle to new x
	turtle.seth(x)
	innerkoch(iter)
	x += 120

	# third side of triangle
	turtle.seth(x)
	innerkoch(iter)



### Cantor Set Code

# cantor() - main fractal function
def cantor(iter,l,x,y):
	# iter is number of iterations left to do
	# l is length of line
	# x is initial x of first line
	# y is initial y of first line
	# d is distance between the horizontal lines of cantor set on the y-axis
	turtle.width(1)
	d = 30

	# must end drawing if iter (number of iterations left to do) equals zero
	if iter == 0:
		return

	else:
		# CANTOR SET COLOR
		turtle.colormode(255)
		turtle.pencolor((iter*100)%255, 100, 100)

		# draw line from x,y by l
		turtle.pu()
		turtle.goto(x,y)
		turtle.pd()
		turtle.fd(l)

		# call cantor twice to draw two new lines for the first 1/3 and the third 1/3 of the segment
		# l is divided by 3
		# first 1/3 segment is drawn at the initial x
		# third 1/3 segment is drawn at the two-thirds mark on the original line
		cantor(iter-1, l/3, x, y-d)
		cantor(iter-1, l/3, x+(2*l/3), y-d)



# CALLING ALL CODE TO DRAW FRACTALS

# if user wants to draw koch snowflake
def kochOption():
	kochUser = input("\nHow many iterations of the curve would you like to implement?: ")
	# check if input is a whole number, number of iterations should be such a number
	if float(kochUser)%1 == 0:
		koch(int(kochUser))
		print("\nClick on the image to exit!\n")
	else:
		print("Can't do that number of iterations! Type in a natural number.")
		kochOption()

# if user wants to draw cantor set
def cantorOption():
	# check if input is a whole number, preferable if length of original line is such a number
	cantorUser = input("\nHow long would you like the original line to be?: ")
	if float(cantorUser)%1 == 0:
		cantor(7, int(cantorUser), -350, 300)
		print("\nClick on the fractal image to exit!\n")
	else:
		print("Can't make that the length of the original line! Type in a natural number.")
		cantorOption()

"""
# if user wants to draw pythagoras tree
def pythagOption():
"""

# function for user fractal menu
def drawFractal():
	user = input("\n\n\nWhich fractal would you like to draw?:\n" +
		"1. Koch Snowflake\n" +
		"2. Cantor Set\n\n")
		# "3. Pythagoras Tree\n\n"

	if user == "1":
		# calling code to draw koch snowflake
		kochOption()
	elif user == "2":
		# calling code to draw cantor set
		cantorOption()

		"""
		elif user == "3":
			pythagOption()
		"""
	else:
		print("\nThat option is not available! Please input 1 or 2.\n")
		drawFractal()

	# turtle module quits automatically after completing drawing without turtle.exitonclick
	# exits program after user clicks on module screen
	turtle.exitonclick()

# calling function to display user fractal menu
# drawFractal()



# Pythagoras Tree
"""
def square(w, x, y):
	turtle.pd()
	for i in range(4):
		turtle.fd(w)
		turtle.left(90)
	turtle.pu()

#
def squareL(w, x, y):
	turtle.pu()
	turtle.goto(x,y)
	turtle.pd()
	turtle.fd(w)
	turtle.right(90)
	turtle.fd(w)
	turtle.right(90)
	turtle.fd(-w)
	turtle.right(90)
	turtle.fd(-w)
	turtle.right(90)
	turtle.fd(w)
	turtle.pu()
#

def main(iter, w, x, y):
	turtle.pu()
	turtle.goto(x,y)
	turtle.pd()
	# original square
	square(w, x, y)

	# drawing subsequent iterations
	tree(iter, w, x, y)
	turtle.pu()

	# --turtle.goto(x-w, y)
	# --square(w, x-w, y)


def tree(iter, w, x, y):
	global X
	# end if iterations are complete
	if iter == 0:
		return
	else:
		turtle.rt(90)
		turtle.fd(-w)

		x = x - (1/2)*x
		y = y + (1/2)*y

		X = x
		Y = y
		turtle.rt(-135)
		
		square(w/sqrt(2), x, y)

		turtle.pu()
		turtle.goto(x+w, y)
		turtle.pd()

		square(w/sqrt(2), x, y)

		tree(iter-1, w/sqrt(2), X, Y)


		#
		turtle.rt(45)
		squareR(w, x, y)
		
		turtle.rt(-90)
		squareL(w, x, y)

		tree(iter-1, w/sqrt(2), x-(1/2)*w, y-(1/2)*w)
		tree(iter-1, w/sqrt(2), x+(1/2)*w, y+(1/2)*w)
		#

main(2, 50, 0, 100)
"""

# tree(2, 50, 0, 100)

# squareR(50, 100, 100)

#####
"""
turtle.pd()
turtle.shape("square")
turtle.shapesize(w,w)
turtle.pu()
turtle.tilt(45)
turtle.goto(100,100)
turtle.shape('square')
# turtle.tilt(45)
turtle.shapesize(w,w)
"""
#######

#######

""""
def mainsq(iter, w, x, y):
	turtle.pd()
	turtle.shapesize(w/sqrt(2))
	turtle.shape("square")
	turtle.stamp()

	# W=200
	turtle.pu()

	pythag(iter-1, w/sqrt(2), x,y)
	# pythag(iter-1, x+(1/2)*w, y+(1/2)*w)

def pythag(iter, w, x, y):
	global W
	# W=200
	if iter == 0:
		return
	else:
		x = x+(1/4)*w/sqrt(2)
		y= y+(sqrt(2)/4)*w
		turtle.pu()
		turtle.goto(x,y)
		turtle.pd()
		turtle.tilt(45)
		turtle.shapesize(w/sqrt(2))
		turtle.shape("square")
		turtle.stamp()
		turtle.pu()
		# turtle.rt(-45)

		pythag(iter-1, w/sqrt(2), x,y)

	###
	square = ((0,0),(10,0), (10,10), (0,10))
	s = turtle.Shape("compound")
	s.addcomponent(square, "red", "blue")

	turtle.register_shape("square", square)
	###

mainsq(4, 10, 50, 50)
"""
turtle.width(5)

"""
def innersquare(w):
	for i in range(4):
		turtle.fd(w/sqrt(2))
		turtle.right(90)

	Ptree(iter, w)

def Ptree(iter, w):
	if iter == 0:
		turtle.rt(225)
		turtle.fd(w)

	else:
		turtle.rt(90)
		turtle.fd(w)

		turtle.pd()
		turtle.left(90)
		turtle.fd(w)

		turtle.rt(-45)
		innersquare(w)

		turtle.rt(135)
		turtle.fd(w)

		turtle.rt(-135)
		innersquare(w)


		Ptree(iter-1, w)
"""

def fancy_square(iter, w):
	turtle.fd(w)
	turtle.rt(90)
	if iter > 0:
		turtle.rt(-135)
		newW = w/sqrt(2)
		fancy_square(iter-1, newW)
		turtle.rt(135)
	turtle.fd(w)
	turtle.rt(90)

	if iter > 0:
		turtle.rt(-225)
		newW = w/sqrt(2)
		turtle.fd(newW)
		turtle.rt(90)
		fancy_square(iter-1, newW)
		turtle.fd(newW)
		turtle.rt(90)
		turtle.fd(newW)
		turtle.rt(90)
		turtle.fd(newW)
		turtle.rt(90)
		turtle.rt(225)
	turtle.fd(w)
	turtle.rt(90)
	turtle.fd(w)
	turtle.rt(90)

turtle.rt(-90)
fancy_square(7, 100)

"""
def fancy_square(iterations, sidelength)
	move sidelength
	rotate 90
	if(iterations > 0)
		rotate to starting angle
		calculate new_sidelength
		fancy_square(iterations-1, new_sidelength)
	move sidelength
	rotate 90
	if(iterations > 0)
		rotate to starting angle
		calculate new_sidelength
		fancy_square(iterations-1, new_sidelength)
	move sidelength
	rotate 90
	move sidelength
	rotate 90
"""

"""
turtle.rt(225)
turtle.fd(w)

turtle.rt(90)
turtle.fd(w)
"""
"""
for i in range(4):
	turtle.left(90)
	turtle.fd(w)
turtle.pu()
"""

# Ptree(2, 100)

turtle.exitonclick()

