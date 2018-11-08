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


# initial length
global l
l = 50

# x is original heading
x = 0
y = x + 60
z = x - 60

# turtle.pu() - pull the pen up, no drawing when moving
turtle.pu()
turtle.goto(-100, -200);
# turtle.pd() - pull the pen down, drawing when moving
turtle.pd()


def innerkoch(n):
	global x, y, z

	if n == 0:
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
	koch(3)


main()

turtle.exitonclick()




