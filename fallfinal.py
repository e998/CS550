# Esther Sojung An
# 11/14/2018
# Fall Final Project: More Fractals!
# It was challenging to work with these fractals and to understand specific patterns, but it was really cool and rewarding. Learning turtle was a fun process and I loved working with it! There were some aspects, including when I was attempting to draw squares for the Pythagoras tree, that were difficult to understand when using the module. Other sections, however, like the koch snowflake, were a lot easier to complete with the use of turtle and made more sense logically. Working with pseudo-code was very important for this project and took a lot of time because I had to understand what the objective of each function was before going in and trying to complete something. I had a lot of code that didn’t end of working, and it took numerous drafts, but I learned a lot about the thinking process behind completing these problems!

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
	turtle.pencolor( (100*N + 10)%255, (N+50)%255, 200)

	# must begin drawing if n (number of iterations left to do) equals zero
	if n == 0:
		# change N variable to shift turtle.pencolor for gradient
		N += 20
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
	turtle.seth(0)
	turtle.width(2)
	d = 30

	# must end drawing if iter (number of iterations left to do) equals zero
	if iter == 0:
		return

	else:
		# CANTOR SET COLOR
		# color depends on iteration, forms a gradient
		turtle.colormode(255)
		turtle.pencolor((iter*25)%255, 100, 170)

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
s


### Pythagoras Tree Code

def tree(iter, w):
	turtle.width(7)
	global N # used for changing some colors in pythagoras
	N +=30

	# PYTHAGORAS COLOR, for left squares
	turtle.colormode(255)
	turtle.pencolor((iter*153 + 40)%255, (iter*3 + 30)%255, (iter*100 + 35)%255)

	# initial line drawn up for the first side of the first iteration
	turtle.fd(w)
	turtle.rt(90)

	# if iter (number of iterations left) is not yet 0, draw the left square of the next iteration
	if iter > 0:
		turtle.rt(-135)
		newW = w/sqrt(2)
		tree(iter-1, newW)
		turtle.rt(135)
	# move forward the length of the previous iteration's square to a new position for the right square of the next iteration
	turtle.fd(w)
	turtle.rt(90)

	# PYTHAGORAS COLOR continued, for right squares
	turtle.colormode(255)
	turtle.pencolor((N*3)%255, 100, 200)

	# if iter (number of iterations left) is still not 0, draw the right square of the next iteration
	if iter > 0:
		turtle.rt(-225)
		newW = w/sqrt(2)
		# draw up the first side of the right square
		turtle.fd(newW)
		turtle.rt(90)
		# draw the rest of the right square to end at the top right corner of the previous iteration's square
		tree(iter-1, newW)
		# pull pen up to move turtle around right square to position at intersection of left square and right square for next iteration
		turtle.pu()
		turtle.fd(newW)
		turtle.rt(90)
		turtle.fd(newW)
		turtle.rt(90)
		turtle.fd(newW)
		turtle.rt(90)
		turtle.rt(225)
		turtle.pd()
	# if iter (number of iterations left) is no longer 0
	# finish the first iteration by drawing down and to the left for the remaining two sides of the square not yet drawn
	turtle.fd(w)
	turtle.rt(90)
	turtle.fd(w)
	turtle.rt(90)

# from the very beginning, rotate turtle so it is facing up in the correct direction
turtle.rt(-90)


""" Pythagoras Tree pseudo-code
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
	cantorUser = input("\nHow many iterations of the set would you like to implement?: ")
	if float(cantorUser)%1 == 0:
		cantor(int(cantorUser), 690, -350, 300)
		print("\nClick on the fractal image to exit!\n")
	else:
		print("Can't do that number of iterations! Type in a natural number.")
		cantorOption()

# if user wants to draw pythagoras tree
def pythagOption():
	pythagUser = input("\nHow many iterations of the tree would you like to implement?: ")
	# check if input is a whole number, preferable if length of original line is such a number
	if float(pythagUser)%1 == 0:
		tree(int(pythagUser), 100)
		print("\nClick on the fractal image to exit!\n")
	else:
		print("Can't do that number of iterations! Type in a natural number.")
		pythagOption()


# function for user fractal menu
def drawFractal():
	user = input("\n\n\nWhich fractal would you like to draw?:\n" +
		"1. Koch Snowflake\n" +
		"2. Cantor Set\n" + 
		"3. Pythagoras Tree\n\n")

	if user == "1":
		# calling code to draw koch snowflake
		kochOption()
	elif user == "2":
		# calling code to draw cantor set
		cantorOption()
	elif user == "3":
		# calling code to draw pythagoras tree
		pythagOption()
	else:
		print("\nThat option is not available! Please input 1 or 2.\n")
		drawFractal()

	# turtle module quits automatically after completing drawing without turtle.exitonclick
	# exits program after user clicks on module screen
	turtle.exitonclick()

# calling function to display user fractal menu
drawFractal()




