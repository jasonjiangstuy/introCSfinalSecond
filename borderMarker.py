import PIL
from PIL import Image
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
import numpy as np
import math
import colorsys
# marker color
value = 0.5

tolerance = 1

targetColor =  (0,1.0,1.0) # dummy red
import numpy as np

width = 700
img = Image.open('hard.jpg')
wpercent = (width/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((width,hsize))#, PIL.Image.BOX
img.show()

#all x colored pixels that have been found
foundAlready = {}
foundBlobs = []

def close(hsv):
   global targetColor
   global tolerance
   hue, sat, val = hsv
   total = 0
   total += hue - targetColor[0]
   total += sat - targetColor[1]
   total += val - targetColor[2]
   return (total < tolerance)
   
def getPoint(first, second):
    
class myMarker():
    def __init__(self, startPoint):
        self.allPixels = []
        self.top = startPoint
    def add(self, x):
        self.allPixels.append(x)
    def lens(self):
        return len(self.allPixels)
    def getEdge(self, img):
      #  on left side of img
       if img.width/2 > self.top[0]: 
          if img.height/2 > self.top[1]:
            #  top
            Mleft = min(self.allPixels, key= lambda x: getPoint(x))
            Mtop = min(self.allPixels, key=lambda x: x[1])
            
            Mright = max(self.allPixels, key=lambda x: x[0])
            Mbot = max(self.allPixels, key=lambda x: x[1])
          else:
            #  bottom
       else:
          if img.height/2 > self.top[1]:
            #  top
          else:
            #  bottom


def findSurrounding(startCoord, letterObject):
    global foundAlready
    myObject = letterObject
    # print(startCoord)
    # print('newblob')
    #to avoid a recursion depth error, using a queue
    stack = [startCoord]
    width, height = blackAndWhite.size
    for i in stack:
        if i not in foundAlready:
            # print(i)
            startCoord = i 
            foundAlready[startCoord] = ''
            myObject.add(startCoord)

            # black right pixel
            if (startCoord[0] + 1 < width):
               testPixel =  (startCoord[0] + 1, startCoord[1]) 
               if blackAndWhite.getpixel(testPixel) == 0 and testPixel not in foundAlready:
                  stack.append( testPixel )
            # black bottom pixel
            if (startCoord[1] + 1 < height):
               testPixel =  (startCoord[0] , startCoord[1] + 1) 
               if blackAndWhite.getpixel(testPixel) == 0 and testPixel not in foundAlready:
                  stack.append( testPixel )
            # black left pixel
            if (startCoord[0] - 1 < 0):
               testPixel =  (startCoord[0] - 1 , startCoord[1]) 
               if blackAndWhite.getpixel(testPixel) == 0 and testPixel not in foundAlready:
                  stack.append( testPixel )
        stack = stack[1:]
    return myObject

for x in range(img.width):
      for y in range(img.height):
         if close(colorsys.rgb_to_hsv(img.getpixel( (x,y) )):
            foundBlobs = findSurrounding(startPoint, myMarker(x,y))

if len(foundBlobs) > 0:
   redBlob = max(foundBlobs, key=lambda x: x.lens())
else:
   # fail, marker not found
    return (False)



# array = np.array(img)
# print(array)
# # [ 0.21069679  0.61290182  0.63425412  0.84635244  0.91599191  0.00213826
# #   0.17104965  0.56874386  0.57319379  0.28719469]

# while True:
#    cornerPx = find_nearest(array, value)
   
#    print(cornerPx)



# # 0.568743859261




# getMarker('testImages/difficult.jpg')
# # returns image rotated perfectly