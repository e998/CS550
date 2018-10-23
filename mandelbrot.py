# 10/19/2018
# Mandelbrot

""" SOURCES
colorsys - https://docs.python.org/2/library/colorsys.html
"""

### IMPORTS
# PIL = PILLOW
from PIL import Image
import colorsys

# change values to shift and zoom
# -1.0, 0.0

"""
xmin, xmax = -2.0, 2.0
ymin, ymax = -2.0, 2.0

"""
xmin, xmax = -0.817370927008279343525, -0.817364941727795366608
ymin, ymax = 0.188930795344368481106, 0.188935270320431267586


imgx, imgy = 512, 512

# maximum iterations, color based on number of iterations
maxIt = 256

image = Image.new("RGB", (imgx,imgy))

for y in range(imgy):
	cy = ( y * (ymax-ymin) / (imgy-1) ) + ymin
	for x in range(imgx):
		cx = ( x * (xmax-xmin) / (imgx-1) ) + xmin
		c = complex(cx,cy)
		z = 0
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**2 + c

		r = 2*i%256
		g = (i*500)%256 #(i*50)%256
		b = (256-i) #256-i

		# converting between color systems with colorsys - rgb to hsv

		#h,l,s = colorsys.rgb_to_hls(r,g,b)

		# could just write: image.putpixel((x,y),(i,0,0)) 
		image.putpixel((x,y),(r,g,b))

image.show()




