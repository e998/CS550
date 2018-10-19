# 10/19/2018 HW
# Mandelbrot

# PIL = PILLOW
from PIL import Image

import random as r

imgx = 512
imgy = 512

# tuple is width and height of picture - (imgx, imgy)
mandelbrot = Image.new("RGB",(imgm, imgn))

# variable.putpixel((how far over, how far down), (color))

n = 0

for i in range(1,255):
	if i <=255
		True
	else
		False

while mandelbrot == True:
	for a in range(-256,256):
		for b in range(-256,256):
			c = (a,b)

			x = r.randint(-256,256)
			y = r.randint(-256,256)

			# length of z
			z = (x**2 + y**2)**(0.5)

			# Z = z**2
			Z = (x**2 - y**2, 2*x*y)

			# z(n+1) = z(n)**2 + c
			z = Z + c

			n += 1

while mandelbrot == False:
	break
	image.putpixel((x,y),(n,0,0))

mandelbrot.save("mandelbrot.png","PNG")




