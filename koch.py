# Koch Snowflake
# 10/25/2018
# On my honor, I have neither given nor received unauthorized aid.

from PIL import Image
from PIL import Image, ImageDraw
from math import *

imgx, imgy = 512, 512
koch = Image.new("RGB", (imgx,imgy))

draw = ImageDraw.Draw(koch)

def distance(pA, pB):
	return sqrt((pA[0]-pB[0])**2 + (pA[1]-pB[1])**2)

def normal(distance):
	m = float(distance())
	if m != 0:
   		div(m)

# def gogoFractal(pA, pB, pC):
def gogoFractalAB(pA, pB):
	global h, lx, ly, rx, ry, tx, ty

	# t = 1/3
	lx = ((2/3)*pA[0] + (1/3)*pB[0])
	ly = ((2/3)*pA[1] + (1/3)*pB[1])
	left = ( lx , ly )

	# t = 2/3
	rx = ((1/3)*pA[0] + (2/3)*pB[0])
	ry = ((1/3)*pA[1] + (2/3)*pB[1])
	right = ( rx , ry )

	# drawing PA to PB without middle section
	draw.line(((pA[0], pA[1]), (lx, ly)), fill=128)
	draw.line(((rx,ry), (pB[0], pB[1])), fill=128)

	# height of the triangle

	if pA[1]==pB[1] or ly == ry:
		h = float(((sqrt(3))/2) * (1/3) * (distance( (pA[0],pA[1]) , (pB[0],pB[1]) )))
	else:
		h = float(((sqrt(3))/2) * (1/3) * (distance( (pA[0],pA[1]) , (pB[0],pB[1]) )))

	# midpt of triangle
	mx = (pA[0]+pB[0])/2
	my = (pA[1]+pB[1])/2
	midpt = (mx, my)

	# slope of triangle line
	slope = (pB[1]-pA[1]) / (pB[0]-pA[0])

	# slope of triangle height
	hSlope = -1/slope

	# top of triangle 1
	tx = int(mx - (h/2)*sqrt(3))
	ty = int(my-(h/2))

	koch.putpixel((tx,ty),(255, 0, 0))

	draw.line(((lx, ly), (tx, ty)), fill=128)
	draw.line(((rx, ry), (tx, ty)), fill=128)


	# redefining points for 2nd iteration


""" pseudo-code for gogoFractal
def gogoFractal(pA, pB, pC):
        # between A and B, calculate 1/3 (D) and 2/3(E) points
        # draw between A and 1/3(D), and 2/3(E) and B
        # h is the height of the slanty triangle
        gogoFractal(D, E, h)
        # do the same process for B and C, and then C and A
"""

def gogoFractalCA(pA, pC):
	global h, lx, ly, rx, ry, tx, ty

	# t = 1/3
	lx = ((2/3)*pC[0] + (1/3)*pA[0])
	ly = ((2/3)*pC[1] + (1/3)*pA[1])
	left = ( lx , ly )

	# t = 2/3
	rx = ((1/3)*pC[0] + (2/3)*pA[0])
	ry = ((1/3)*pC[1] + (2/3)*pA[1])
	right = ( rx , ry )

	# drawing PA to PB without middle section
	draw.line(((pC[0], pC[1]), (lx, ly)), fill=128)
	draw.line(((rx,ry), (pA[0], pA[1])), fill=128)

	# height of the triangle

	if pC[1]==pA[1] or ly == ry:
		h = float(((sqrt(3))/2) * (1/3) * (distance( (pC[0],pC[1]) , (pA[0],pA[1]) )))
	else:
		h = float(((sqrt(3))/2) * (1/3) * (distance( (pC[0],pC[1]) , (pA[0],pA[1]) )))

	# midpt of triangle
	mx = (pC[0]+pA[0])/2
	my = (pC[1]+pA[1])/2
	midpt = (mx, my)


	# top of triangle 1
	tx = int(mx + (h/2)*sqrt(3))
	ty = int(my-(h/2))

	koch.putpixel((tx,ty),(255, 0, 0))

	draw.line(((lx, ly), (tx, ty)), fill=128)
	draw.line(((rx, ry), (tx, ty)), fill=128)




def gogoFractalBC(pB, pC):
	global h, lx, ly, rx, ry, tx, ty

	# t = 1/3
	lx = ((2/3)*pC[0] + (1/3)*pB[0])
	ly = ((2/3)*pC[1] + (1/3)*pB[1])
	left = ( lx , ly )

	# t = 2/3
	rx = ((1/3)*pC[0] + (2/3)*pB[0])
	ry = ((1/3)*pC[1] + (2/3)*pB[1])
	right = ( rx , ry )

	# drawing PA to PB without middle section
	draw.line(((pC[0], pC[1]), (lx, ly)), fill=128)
	draw.line(((rx,ry), (pB[0], pB[1])), fill=128)

	# height of the triangle
	if pC[1]==pB[1] or ly == ry:
		h = float(((sqrt(3))/2) * (1/3) * (distance( (pC[0],pC[1]) , (pB[0],pB[1]) )))
	else:
		h = float(((sqrt(3))/2) * (1/3) * (distance( (pC[0],pC[1]) , (pB[0],pB[1]) )))

	# midpt of triangle
	mx = (pC[0]+pB[0])/2
	my = (pC[1]+pB[1])/2
	midpt = (mx, my)

	# top of triangle 1
	tx = int(mx)
	ty = int(my+(h/2)*sqrt(3))

	koch.putpixel((tx,ty),(255, 0, 0))

	draw.line(((lx, ly), (tx, ty)), fill=128)
	draw.line(((rx, ry), (tx, ty)), fill=128)





# gogoFractal((x1, y1), (x2, y2), (x3, y3))

# pA to pB
gogoFractalAB((imgx/2, 140), (imgx/2 - 125, 140 + 125*sqrt(3)))

# pB to pC
gogoFractalBC((imgx/2 - 125, 140 + 125*sqrt(3)), (imgx/2 + 125, 140 + 125*sqrt(3)))

# pC to pA
gogoFractalCA((imgx/2 + 125, 140 + 125*sqrt(3)), (imgx/2, 140))


gogoFractalAB((imgx/2, 140), (lx,ly))
# gogoFractalAB((imgx/2 - 125, 140 + 125*sqrt(3)), (rx,ry))

# need to do this after redefining variables and recursion?
gogoFractalAB((lx,ly), (tx,ty))
# gogoFractalAB((tx,ty), (rx,ry))

# fractal(0,10,10,30)

koch.show()




