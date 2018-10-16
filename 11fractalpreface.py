# PIL = PILLOW
from PIL import Image

imgx = 512
imgy = 512

# tuple is width and height of picture - (imgx, imgy)
image = Image.new("RGB",(imgx, imgy))

# variable.putpixel((how far over, how far down), (color))
for i in range(512):
	for j in range(512):
		image.putpixel((i,j),(255-int(i*(1/2)),0,0))

for i in range(462):
	for j in range(462):
		image.putpixel((i,j),(0+int(i*(1/3)),0, 0))

for i in range(412):
	for j in range(412):
		image.putpixel((i,j),(255-int(i*(2/3)),0, 0))

for i in range(362):
	for j in range(362):
		image.putpixel((i,j),(0+int(i*(1/3)),0, 0))

for i in range(312):
	for j in range(312):
		image.putpixel((i,j),(255-int(i*(5/6)),0, 0))

for i in range(262):
	for j in range(262):
		image.putpixel((i,j),(0+int(i*(2/3)),0, 0))

for i in range(212):
	for j in range(212):
		image.putpixel((i,j),(255-int(i*(100000/100001)),0, 0))

for i in range(162):
	for j in range(162):
		image.putpixel((i,j),(0+int(i*(1.5)),0, 0))

for i in range(112):
	for j in range(112):
		image.putpixel((i,j),(255-int(i*(2)),0, 0))

for i in range(62):
	for j in range(62):
		image.putpixel((i,j),(0+int(i*(3.5)),0, 0))


image.save("fractaldemo.png","PNG")






