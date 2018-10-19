# 10/16/2018

# PIL = PILLOW
from PIL import Image

"""
# Checkerboard!

imgx = 100
imgy = 100
w = 10
n = 10

square = Image.new("RGB",(imgx, imgy))

for a in range(imgx):
	for b in range(imgy):
		if a%20 < 10:
			if b%20 < 10:
				square.putpixel((a,b),(0,0,0))
			else:
				square.putpixel((a,b),(255,0,0))
		else:
			if b%20 >= 10:
				square.putpixel((a,b),(0,0,0))
			else:
				square.putpixel((a,b),(255,0,0))

square.save("checkerboard.png","PNG")
"""











"""
os.chdir(r"CS550 estheran$ python3 11fractalpreface.py")
os.startfile("fractaldemo.png")
"""

