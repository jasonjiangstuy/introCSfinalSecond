import PIL
from PIL import Image
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
import numpy as np

img = Image.open('Annotation 2020-06-07 170005.jpg')

#credit to https://predictivehacks.com/iterate-over-image-pixels/ to show how to iterate in PIL
# greyscale
blackAndWhite = img.convert("L")

for x in range(img.width):
    for y in range(img.height):
        if blackAndWhite.getpixel( (x,y) )< 100: 
            # set to black
            blackAndWhite.putpixel( (x,y) ,0)
        else:
            # set to white
            blackAndWhite.putpixel( (x,y) ,255)

testPixel = blackAndWhite.getpixel( (startCoord[0] + 1, startCoord[1]) )
print(testPixel)
(68, 115)