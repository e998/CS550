# 11/2/2018

""" Sources:
- Turtle module - https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.radians
- Koch Snowflake pseudo-code - https://scratch.mit.edu/projects/110378199/#editor
"""

### Imports
from math import *
import turtle
# from turtle import *

"""
turtle.pd()
Pull the pen down – drawing when moving.

turtle.pu()
Pull the pen up – no drawing when moving.
"""

"""
# distance formula
def distance(pA, pB):
	return sqrt( (pA[0]-pB[0])**2 + (pA[1]-pB[1])**2 )

def gogoFractalAB(pA, pB):
	global h, lx, ly, rx, ry, tx, ty
	# t = 1/3
	lx = ((2/3)*pA[0] + (1/3)*pB[0])
	ly = ((2/3)*pA[1] + (1/3)*pB[1])
	left = (lx, ly)

	# t = 2/3
	rx = ((1/3)*pA[0] + (2/3)*pB[0])
	ry = ((1/3)*pA[1] + (2/3)*pB[1])
	right = (rx, ry)

AX = 200
AY = 200
BX = 500
BY = 200

# t = 1/3
lx = ((2/3)*AX + (1/3)*BX)
ly = ((2/3)*AY + (1/3)*BY)
left = (lx, ly)

# position(A,B)
# distance((0,0) , (pA[0],pA[1]))

# gogoFractalAB((AX,AY),(lx,ly))


distance( (0,0), (AX,AY) )
turtle.towards(AX,AY)

# turtle.forward(distance((AX,AY), left))
"""


# initial length
global l
l = 30

# x is original heading
x = 0
y = x + 60
z = x - 60

# print(turtle.heading())
turtle.pu()
turtle.goto(-300, -250);
turtle.pd()

def innerkoch():
	global l
	# global iter
	# for i in range(3):
	l = l/3
	#if iter == 0:
	turtle.fd(l)
	#else:
	# innerkoch(iter-1)
	turtle.seth(x)
	turtle.fd(l)
	turtle.seth(y)
	turtle.fd(l)
	turtle.seth(z)
	turtle.fd(l)
	turtle.seth(x)
	turtle.fd(l)
	# iter = iter - 1
	# innerkoch()


# def koch(iter):
def koch():
	innerkoch()
	# turtle.seth = turtle.setheading
	# turtle.seth(x)
	# turtle.fd(l)
	global l
	for i in range(3):
		l = 3*l
		turtle.seth(y)
		turtle.fd(l)
		turtle.seth(z)
		turtle.fd(l)
		turtle.seth(x)
		turtle.fd(l)
	

koch()

turtle.exitonclick()


""" pseudo-code for gogoFractal
def gogoFractal(pA, pB, pC):
    # between A and B, calculate 1/3 (D) and 2/3(E) points
    # draw between A and 1/3(D), and 2/3(E) and B
    # h is the height of the slanty triangle
    gogoFractal(D, E, h)
    # do the same process for B and C, and then C and A
"""





