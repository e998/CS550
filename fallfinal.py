# Esther Sojung An
# DUE: 11/13/2018

""" Sources:
- Turtle module - https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.radians
- Koch Snowflake pseudo-code - https://scratch.mit.edu/projects/110378199/#editor
"""

### Imports
from math import *
import turtle
# from turtle import *


""" Koch Snowflake Code
# initial length
global l
l = 50
N = 0

# x is original heading
x = 0
y = x + 60
z = x - 60

# turtle.pu() - pull the pen up, no drawing when moving
turtle.pu()
turtle.goto(-100, -200)
# turtle.pd() - pull the pen down, drawing when moving
turtle.pd()


def innerkoch(n):
	global x, y, z, N
	turtle.colormode(255)
	turtle.pencolor( (100*N + 10)%255, 200, 100)
	if n == 0:
		N += 10
		turtle.fd(l/3)

	else:
		turtle.seth(x)
		innerkoch(n-1)

		x -= 60

		turtle.seth(x)
		innerkoch(n-1)

		x += 120

		turtle.seth(x)
		innerkoch(n-1)

		x -= 60

		turtle.seth(x)
		innerkoch(n-1)


def koch(iter):
	global l, x, y, z
	# turtle.seth = turtle.setheading
	innerkoch(iter)
	x += 120
	turtle.seth(x)
	innerkoch(iter)
	x += 120
	turtle.seth(x)
	innerkoch(iter)


def main():
	l = 50
	koch(2)


main()
"""


# Cantor Set Code

w = 90
X = 0
Y = 0
d = 10


def main():
	turtle.pd()
	turtle.goto(X, Y)
	turtle.fd(w)

	innercantor()


def innercantor():
	global w, X, Y

	if w <= 0.5:
		turtle.done()

	else:
		w = w/3
		turtle.pu()
		turtle.goto(X, Y-d)

		turtle.pd()
		turtle.fd(w)

		turtle.pu()
		turtle.goto(X+2*w, Y-d)

		turtle.pd()
		turtle.fd(w)

		Y = Y - d

	innercantor()


main()


turtle.exitonclick()




