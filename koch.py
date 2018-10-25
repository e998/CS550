# Koch Snowflake

from PIL import Image
from PIL import Image, ImageDraw
from math import *

imgx, imgy = 512, 512

koch = Image.new("RGB", (imgx,imgy))

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

draw = ImageDraw.Draw(koch)

draw.line(((0, 0),(100,100)), fill=128)


# ((1−t)a1+tb1,(1−t)a2+tb2
# fractal(0,10,10,30)
koch.show()




