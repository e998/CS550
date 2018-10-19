# 10/19/2018
# Mandelbrot

# PIL = PILLOW
from PIL import Image

# change values to shift and zoom
# -1.0, 0.0
xmin, xmax = -2.0, 2.0
ymin, ymax = -2.0, 2.0

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

		r = (i*5)%256
		g = (256-2*i)%256 #(i*50)%256
		b = (i*100)%256 #256-i

		# could just write: image.putpixel((x,y),(i,0,0)) 
		image.putpixel((x,y),(r,g,b))

image.show()




