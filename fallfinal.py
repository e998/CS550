# Esther Sojung An
# DUE: 11/14/2018

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



""" Cantor Set Code

def cantor(iter,w,x,y):
	global d

	if iter == 0:
		return
		# turtle.done()
	else:
		#draw line from x,y by w
		turtle.pu()
		turtle.goto(x,y)
		turtle.pd()
		turtle.fd(w)

		cantor(iter-1, w/3, x, y-10)
		cantor(iter-1, w/3, x+(2*w/3), y-10)

cantor(7, 700, -350,300)
"""



# Pythagoras Tree

def squareR(w, x, y):
	turtle.pu()
	turtle.goto(x,y)
	turtle.pd()
	turtle.fd(-w)
	turtle.left(90)
	turtle.fd(-w)
	turtle.left(90)
	turtle.fd(-w)
	turtle.left(90)
	turtle.fd(-w)
	turtle.pu()
	
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

def main(w, x, y):
	turtle.pd()
	squareR(w, x, y)
	turtle.pu()
	turtle.goto(x-w, y)
	squareL(w, x-w, y)

def tree(iter, w, x, y):
	if iter == 0:
		return
	else:
		turtle.rt(45)
		squareR(w, x, y)
		
		turtle.rt(-90)
		squareL(w, x, y)

		tree(iter-1, w/sqrt(2), x-(1/2)*w, y-(1/2)*w)
		tree(iter-1, w/sqrt(2), x+(1/2)*w, y+(1/2)*w)
"""
main(50, 0, 100)
tree(2, 50, 0, 100)
"""
squareL(50, 100, 100)

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

turtle.exitonclick()




