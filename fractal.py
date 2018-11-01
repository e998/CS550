# Esther Sojung An
# 11/1/2018
# Fractals!
# This project was really interesting, and I loved working with fractals. The code, especially for the koch snowflake, could be difficult at times, but I enjoyed the challenge! I plan on continuing my work on the koch snowflake and gaining a deeper understanding of drawing with python and utilizing vectors. Getting to know colorsys was very fun. Going over the math for the Mandelbrot set and the Julia set several times helped me understand the pseudo code, and the concept of iterations made sense while I worked with different colors.

# On my honor, I have neither given nor received unauthorized aid.

""" Sources
colorsys - https://docs.python.org/2/library/colorsys.html
Mandelbrot zoom - http://math.hws.edu/eck/js/mandelbrot/MB.html
ImageDraw module (for koch snowflake) - https://pillow.readthedocs.io/en/3.0.x/reference/ImageDraw.html
Koch Snowflake code inspiration - https://natureofcode.com/book/chapter-8-fractals/
"""

### Imports
# PIL = PILLOW
from PIL import Image # for all fractals
import colorsys # for all fractals
import random as r # for julia set fractal
from math import * # for koch snowflake fractal
from PIL import Image, ImageDraw # for koch snowflake fractal

# image dimensions - for all fractals
imgx, imgy = 512, 512

# maximum iterations, color based on number of iterations - for all fractals
maxIt = 256


####### Mandelbrot Set Fractal 1
# Image.new("RGB", (imgx,imgy)) - creating new image
mandelbrot1 = Image.new("RGB", (imgx,imgy))

# change xmin, xmax, ymin, and ymax values to shift and zoom
xmin1, xmax1 = -1.787772861852499972667, -1.787767673194999972667
ymin1, ymax1 = -0.000001922919999999999, 0.000001962650000000001

for y in range(imgy):
	cy = ( y * (ymax1-ymin1) / (imgy-1) ) + ymin1
	for x in range(imgx):
		cx = ( x * (xmax1-xmin1) / (imgx-1) ) + xmin1
		# c is position
		c = complex(cx,cy)
		z = 0
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**2 + c

		# colorsys values go from 0 to 1, dividing by 256
		r = (i*12)/256
		g = (i*2 + 200)/256
		b = (30 - i*8)/256

		# converting between color systems with colorsys - hsv to rgb
		# hsv is Hue Saturation Value
		r,g,b = colorsys.hsv_to_rgb(r,g,b)

		# putpixel with no color conversion: mandelbrot1.putpixel((x,y),(r,g,b))
		# placing pixel of certain color in (x,y) position
		mandelbrot1.putpixel((x,y),(int(r*256),int(g*256),int(b*256)))

mandelbrot1.show()



####### Mandelbrot Set Fractal 2
mandelbrot2 = Image.new("RGB", (imgx,imgy))

xmin2, xmax2 = -0.759472084594068764123, -0.758799559374020336557
ymin2, ymax2 = -0.076981249062837600697, -0.076308723842789173131

for y in range(imgy):
	cy = ( y * (ymax2-ymin2) / (imgy-1) ) + ymin2
	for x in range(imgx):
		cx = ( x * (xmax2-xmin2) / (imgx-1) ) + xmin2
		c = complex(cx,cy)
		z = 0
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**2 + c

			# switching up color based on if imaginary component of c (cy) is divisible by 2
			if cy % 2 == 0:
				r = (i+10)/256
				g = (i*10)/256
				b = (256-3*i)/256
			else:
				r = (70-i)/256 #(50-i)/256
				g = (100 - i*5)/256
				b = (10 - 3*i)/256

		# colorsys - hsv to rgb
		r,g,b = colorsys.hsv_to_rgb(r,g,b)

		mandelbrot2.putpixel((x,y),(int(r*256),int(g*256),int(b*256)))

mandelbrot2.show()



# Julia Set Fractal
julia = Image.new("RGB", (imgx,imgy))

# switched c value to z value, difference from Mandelbrot - z is now complex(cx,cy)
# position (c) is randomized
# c = complex(r.uniform(-1,1), r.uniform(-1,1))

# set values for c to print specific image
c = complex(-0.39368310911400406,-0.741509416176817)
# used print(c) to determine the specificX and specificY

xmin1, xmax1 = -2.0,2.0
ymin1, ymax1 = -2.0,2.0

for y in range(imgy):
	cy = ( y * (ymax1-ymin1) / (imgy-1) ) + ymin1
	for x in range(imgx):
		cx = ( x * (xmax1-xmin1) / (imgx-1) ) + xmin1
		z = complex(cx,cy)
		for i in range(maxIt):
			if abs(z) >= 2.0: break
			z = z**2 + c

		r = (i+10)/256
		g = (16+2*i)/256
		b = (90*i)/256

		# colorsys - hls to rgb
		# hls is Hue Lightness Saturation
		r,g,b = colorsys.hls_to_rgb(r,g,b)

		julia.putpixel((x,y),(int(r*256),int(g*256),int(b*256)))

julia.show()



####### Koch Snowflake Fractal
koch = Image.new("RGB", (imgx,imgy))

# ImageDraw uses same coordinates as PIL, (0,0) in upper left
draw = ImageDraw.Draw(koch)

# distance formula
def distance(pA, pB):
	return sqrt((pA[0]-pB[0])**2 + (pA[1]-pB[1])**2)

# attempt at normalization code
def normal(distance):
	m = float(distance())
	if m != 0:
   		div(m)

""" pseudo-code for gogoFractal
def gogoFractal(pA, pB, pC):
    # between A and B, calculate 1/3 (D) and 2/3(E) points
    # draw between A and 1/3(D), and 2/3(E) and B
    # h is the height of the slanty triangle
    gogoFractal(D, E, h)
    # do the same process for B and C, and then C and A
"""

# between points A & B, first side of triangle
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

	# drawing PA to PB without middle section
	draw.line(((pA[0], pA[1]), (lx, ly)), fill=128)
	draw.line(((rx,ry), (pB[0], pB[1])), fill=128)

	# height of the triangle in first iteration
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

	# coordinates for top of triangle 1
	tx = int(mx - (h/2)*sqrt(3))
	ty = int(my-(h/2))

	# place pixel at (tx, ty)
	koch.putpixel((tx,ty),(255, 0, 0))

	# draw sides of triange from base line to top of triange (tx, ty)
	draw.line(((lx, ly), (tx, ty)), fill=128)
	draw.line(((rx, ry), (tx, ty)), fill=128)


# between points A & C, second side of triangle
def gogoFractalCA(pA, pC):
	global h, lx, ly, rx, ry, tx, ty

	# t = 1/3
	lx = ((2/3)*pC[0] + (1/3)*pA[0])
	ly = ((2/3)*pC[1] + (1/3)*pA[1])
	left = (lx, ly)

	# t = 2/3
	rx = ((1/3)*pC[0] + (2/3)*pA[0])
	ry = ((1/3)*pC[1] + (2/3)*pA[1])
	right = (rx, ry)

	# drawing PA to PC without middle section
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

	# top of triangle 2
	tx = int(mx + (h/2)*sqrt(3))
	ty = int(my-(h/2))

	koch.putpixel((tx,ty),(255, 0, 0))

	draw.line(((lx, ly), (tx, ty)), fill=128)
	draw.line(((rx, ry), (tx, ty)), fill=128)


# between points B & C, third side of triangle
def gogoFractalBC(pB, pC):
	global h, lx, ly, rx, ry, tx, ty

	# t = 1/3
	lx = ((2/3)*pC[0] + (1/3)*pB[0])
	ly = ((2/3)*pC[1] + (1/3)*pB[1])
	left = (lx, ly)

	# t = 2/3
	rx = ((1/3)*pC[0] + (2/3)*pB[0])
	ry = ((1/3)*pC[1] + (2/3)*pB[1])
	right = (rx, ry)

	# drawing PC to PC without middle section
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

	# top of triangle 3
	tx = int(mx)
	ty = int(my+(h/2)*sqrt(3))

	koch.putpixel((tx,ty),(255, 0, 0))

	draw.line(((lx, ly), (tx, ty)), fill=128)
	draw.line(((rx, ry), (tx, ty)), fill=128)


### Calling gogoFractalAB, gogoFractalBC, gogoFractalCA

# pA to pB
gogoFractalAB((imgx/2, 140), (imgx/2 - 125, 140 + 125*sqrt(3)))

# pB to pC
gogoFractalBC((imgx/2 - 125, 140 + 125*sqrt(3)), (imgx/2 + 125, 140 + 125*sqrt(3)))

# pC to pA
gogoFractalCA((imgx/2 + 125, 140 + 125*sqrt(3)), (imgx/2, 140))

# attempt at triange in line between pA and left point
gogoFractalAB((imgx/2, 140), (lx,ly))

# attempt at triange in line between top of first iteration triangle and right point
gogoFractalAB((tx,ty), (rx,ry))


koch.show()




