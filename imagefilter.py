# 11/16/2018
# Esther Sojung An
# Image Filter

### IMPORTS
from PIL import Image
import colorsys


img1 = Image.open('sky.png')
width, height = img1.size
for x in range(width):
	for y in range(height):
		pixel1 = img1.getpixel((x,y))
		r1 = (pixel1[0] * 5)%255
		g1 = 50 # pixel1[1]
		b1 = pixel1[2]
		# colorsys - hsv to rgb
		# hsv is Hue Saturation Value
		r1,g1,b1 = colorsys.hsv_to_rgb(r1/255,g1/255,b1/255)
		img1.putpixel((x,y),(int(255*r1),int(255*g1),int(255*b1)))
	print("row",x,"done")
print("img1 complete!")

img2 = Image.open('sky.png')
width, height = img2.size
for x in range(width):
	for y in range(height):
		pixel2 = img2.getpixel((x,y))
		r2 = (pixel2[0] * 5)%255
		g2 = 100 # pixel2[1]
		b2 = pixel2[2]
		img2.putpixel((x,y),(r2,g2,b2))
print("img2 complete!")

img3 = Image.open('puppy.png')
width, height = img3.size
for x in range(width):
	for y in range(height):
		pixel3 = img3.getpixel((x,y))
		r3 = (pixel3[0] * 5)%255
		g3 = pixel3[1]
		b3 = pixel3[2]
		# colorsys - hls to rgb
		# hls is Hue Lightness Saturation
		r3,g3,b3 = colorsys.hls_to_rgb(r3/255,g3/255,b3/255)
		img3.putpixel((x,y),(int(255*r3),int(255*g3),int(255*b3)))
print("img3 complete!")

img4 = Image.open('puppy.png')
width, height = img4.size
for x in range(width):
	for y in range(height):
		pixel4 = img4.getpixel((x,y))
		r4 = (pixel4[0] * 5)%255
		g4 = pixel4[1]
		b4 = pixel4[2]
		# colorsys - hsv to rgb
		# hsv is Hue Saturation Value
		r4,g4,b4 = colorsys.hsv_to_rgb(r4/255,g4/255,b4/255)
		img4.putpixel((x,y),(int(255*r4),int(255*g4),int(255*b4)))
print("img4 complete!")

img5 = Image.open('puppy.png')
width, height = img5.size
for x in range(width):
	for y in range(height):
		pixel5 = img5.getpixel((x,y))
		r5 = (pixel5[0] * 5)%255
		g5 = pixel5[1]
		b5 = pixel5[2]
		img5.putpixel((x,y),(r5,g5,b5))
print("img5 complete!")


img1.show()
img2.show()
img3.show()
img4.show()
img5.show()




