# 10/25/2018
# Fractals!

""" SOURCES
colorsys - https://docs.python.org/2/library/colorsys.html
Mandelbrot zoom - http://math.hws.edu/eck/js/mandelbrot/MB.html
"""

### IMPORTS
# PIL = PILLOW
from PIL import Image
import colorsys


imgx, imgy = 512, 512

# maximum iterations, color based on number of iterations
maxIt = 256

mandelbrot1 = Image.new("RGB", (imgx,imgy))
mandelbrot2 = Image.new("RGB", (imgx,imgy))
koch = Image.new("RGB", (imgx,imgy))



####### Mandelbrot Fractal 1
# change xmin, xmax, ymin, and ymax values to shift and zoom
xmin1, xmax1 = -0.817370927008279343525, -0.817364941727795366608
ymin1, ymax1 = 0.188930795344368481106, 0.188935270320431267586

for y in range(imgy):
	cy = ( y * (ymax1-ymin1) / (imgy-1) ) + ymin1
	for x in range(imgx):
		cx = ( x * (xmax1-xmin1) / (imgx-1) ) + xmin1
		c = complex(cx,cy)
		z = 0
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**2 + c

		"""
		r = 2*i%256/256
		g = (i*500)%256/256 #(i*50)%256
		b = (256-i)/256 #256-i
		"""

		r = (i)/256
		g = (i*9)/256 #(i*50)%256
		b = (256-3*i)/256 #256-i

		# converting between color systems with colorsys - rgb to hsv
		#h,l,s = colorsys.rgb_to_hls(r,g,b)


		#r,g,b = colorsys.hls_to_rgb(r,g,b)
		r,g,b = colorsys.hsv_to_rgb(r,g,b)
		# blurriness, alternating colors

		# could just write: image.putpixel((x,y),(i,0,0)) 
		# mandelbrot1.putpixel((x,y),(r,g,b))
		mandelbrot1.putpixel((x,y),(int(r*256),int(g*256),int(b*256)))

mandelbrot1.show()



####### Mandelbrot Fractal 2
"""
xmin2, xmax2 = -0.562661266291329170164, -0.562644107056929170164
ymin2, ymax2 = 0.642991779771537499892, 0.643004649197337499892
"""

xmin2, xmax2 = -0.749955274999999998904, -0.746477499999999999071
ymin2, ymax2 = 0.067210575000000000000, 0.06981370000000000000033

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

		# colorsys values go from 0 to 1, dividing by 256
		r = (i)/256
		g = (i*9)/256 #(i*50)%256
		b = (256-3*i)/256 #256-i

		# converting between color systems with colorsys - rgb to hsv
		r,g,b = colorsys.hsv_to_rgb(r,g,b)

		mandelbrot2.putpixel((x,y),(int(r*256),int(g*256),int(b*256)))

mandelbrot2.show()



####### Koch Snowflake Fractal

draw = ImageDraw.Draw(im)

"""
xmin2, xmax2 = -0.562661266291329170164, -0.562644107056929170164
ymin2, ymax2 = 0.642991779771537499892, 0.643004649197337499892
"""

draw.line((0, im.size[1], im.size[0], 0), fill=128)

koch.putpixel((x,y),(r,g,b))

koch.show()




