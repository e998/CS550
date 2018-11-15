# 11/13/2018
# Image Filter

### IMPORTS
from PIL import Image
import scipy.ndimage
from scipy import misc
import matplotlib.pyplot as plt


"""
pix = img.load()
print(pix([1,1]))
"""

# f.save("puppy",".PNG")

img = Image.open('puppy.png')

plt.imshow(img)
plt.show()

# misc.imsave('./puppy.png', f) # uses the Image module (PIL)

r = (i+10)/256
g = (16+2*i)/256
b = (90*i)/256

# colorsys - hsv to rgb
# hsv is Hue Saturation Value
r,g,b = colorsys.hsv_to_rgb(r,g,b)

gauss_denoised = ndimage.gaussian_filter(noisy, 2)

# med_denoised = ndimage.median_filter(noisy, 3)




