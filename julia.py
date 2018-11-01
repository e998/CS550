from PIL import Image

### IMPORTS
import random as r
import colorsys


imgx, imgy = 512, 512

maxIt = 256

julia = Image.new("RGB", (imgx,imgy))
# position (c) is randomized
# c = complex(r.uniform(-1,1), r.uniform(-1,1))
c = complex(-0.39368310911400406,-0.741509416176817)
# (-0.3580440039784014-0.8566523217789364j)
print(c)
xmin1, xmax1 = -2.0,2.0
ymin1, ymax1 = -2.0,2.0

for y in range(imgy):
	cy = ( y * (ymax1-ymin1) / (imgy-1) ) + ymin1
	for x in range(imgx):
		cx = ( x * (xmax1-xmin1) / (imgx-1) ) + xmin1
		z = complex(cx,cy)
		# print (cx, cy)
		for i in range(maxIt):
			if abs(z) >= 2.0: break
			z = z**2 + c

		r = (i+10)/256
		g = (16+2*i)/256
		b = (90*i)/256

		r,g,b = colorsys.hls_to_rgb(r,g,b)

		julia.putpixel((x,y),(int(r*256),int(g*256),int(b*256)))

julia.show()




