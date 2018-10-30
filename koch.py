# Koch Snowflake
# 10/25/2018
# On my honor, I have neither given nor received unauthorized aid.

from PIL import Image
from PIL import Image, ImageDraw
from math import *

imgx, imgy = 512, 512

koch = Image.new("RGB", (imgx,imgy))

"""
def distance(x1,x2,y1,y2):
	return sqrt((x1-x2)**2 + (y1-y2)**2)

def fractal(x1,x2,y1,y2):
	# global koch
	for i in range(x1,x2):
		koch.putpixel((i,y2-y1), (255,0,0))
	for i in range(int(distance(x1,x2,y1,y2)+1)):
		x2 = x1 + cos(pi/3)*i
		y2 = y1 + sin(pi/3)*i
		koch.putpixel((int(x2),int(y2)), (255,0,0))
"""

draw = ImageDraw.Draw(koch)

# draw.line(((0, 0),(100,100)), fill=128)

def distance(pA, pB):
	return sqrt((pA[0]-pB[0])**2 + (pA[1]-pB[1])**2)

def normal(distance):
	m = float(distance())
	if m != 0:
   		div(m)

# def gogoFractal(pA, pB, pC):
def gogoFractal(pA, pB):
	global height
	# draw.line( (x1,y1), (x2,y2), fill=value )
	draw.line(((pA[0], pA[1]), (pB[0], pB[1])), fill=128)

	# t = 1/3
	lx = ((2/3)*pA[0] + (1/3)*pB[0])
	ly = ((2/3)*pA[1] + (1/3)*pB[1])
	left = ( lx , ly )

	# t = 2/3
	rx = ((1/3)*pA[0] + (2/3)*pB[0])
	ry = ((1/3)*pA[1] + (2/3)*pB[1])
	right = ( rx , ry )

	# height of the triangle
	h = float(((sqrt(3))/2) * (1/3) * (distance((imgx/2, 140), (imgx/2 - 125, 140 + 125*sqrt(3)))))


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


	# top point of triangle
	"""
	draw.line(distance((mx, my), (hx, hy))
	pA[0]*pB[0] + pA[1]*
	if mx*hx + my*hx == 0
	"""

	"""
	X = mx - (cos(hSlope))*(float(height))
	Y = my - (sin(hSlope))*(float(height))
	"""

	"""
	X = mx - (cos(pi/4))*height
	Y = my - (sin(pi/4))*height
	"""



"""
def perpBisect(aX, aY, bX, bY, height):
    vX = bX-aX
    vY = bY-aY
    #print(str(vX)+" "+str(vY))
    if(vX == 0 or vY == 0):
        return 0, 0, 0, 0
    mag = sqrt(vX*vX + vY*vY)
    vX = vX / mag
    vY = vY / mag
    temp = vX
    vX = 0-vY
    vY = temp
    cX = bX + vX * height
    cY = bY + vY * height
    dX = bX - vX * height
    dY = bY - vY * height
    return int(cX), int(cY), int(dX), int(dY)

    koch.putpixel((int(vX),int(vY)),(255, 0, 0))

perpBisect(10,100, 20,110, 10)
"""


"""
	Y-my = (-1/slope)(X-mx) 
	((sqrt(3))/2) * distance((mx, my), (X, Y)) = height
"""


""" pseudo-code for gogoFractal
def gogoFractal(pA, pB, pC):
        # between A and B, calculate 1/3 (D) and 2/3(E) points
        # draw between A and 1/3(D), and 2/3(E) and B
        # h is the height of the slanty triangle
        gogoFractal(D, E, h)
        # do the same process for B and C, and then C and A
"""

# gogoFractal((x1, y1), (x2, y2), (x3, y3))
gogoFractal((imgx/2, 140), (imgx/2 - 125, 140 + 125*sqrt(3)))


# fractal(0,10,10,30)
koch.show()




