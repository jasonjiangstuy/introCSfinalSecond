import PIL
from PIL import Image
import requests
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
import numpy as np
import math


# globals

#all black pixels that have been found
foundAlready = {}
# The image
blackAndWhite = None
#to identify the connected black letters from the top right corner -> first left

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

            # checking for:
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
            # black bottom left pixel
            if (startCoord[1] + 1 < height) and (startCoord[0] - 1 < 0):
               testPixel =  (startCoord[0] - 1 , startCoord[1] + 1) 
               if blackAndWhite.getpixel(testPixel) == 0 and testPixel not in foundAlready:
                  stack.append( testPixel )
            
            # black bottom right pixel
            if (startCoord[1] + 1 < height) and (startCoord[0] + 1 < width):
               testPixel =  (startCoord[0] + 1 , startCoord[1] + 1) 
               if blackAndWhite.getpixel(testPixel) == 0 and testPixel not in foundAlready:
                  stack.append( testPixel )
            
        stack = stack[1:]
    return myObject

            
            
class myletter():
    def __init__(self, startPoint):
        self.allPixels = []
        self.top = startPoint[1]
    def add(self, x):
        self.allPixels.append(x)
        # print(self.allPixels)

#find the bounds of the sentence
    def findExtremes(self):
        rightest, lowest = self.allPixels[0]
        leftest = rightest
        for x,y in self.allPixels:
            if lowest < y:
                lowest = y
            if rightest < x:
                rightest = x
            if leftest > x:
                leftest = x
        highest = self.top
        return leftest, rightest, lowest, highest

            
def removeHandwriting(fileObj, backColor):
    import time
    starttime = time.time()
    # URL = "https://www.timeanddate.com/scripts/cityog.php?title=Current%20Local%20Time%20in&amp;city=New%20York&amp;state=New%20York&amp;country=USA&amp;image=new-york1"
    # response = requests.get(URL)
    # img = Image.open(BytesIO(response.content))
    img = fileObj
    # img.save('before.jpg')
    #credit to https://predictivehacks.com/iterate-over-image-pixels/ to show how to iterate in PIL
    # greyscale
    global blackAndWhite 
    blackAndWhite = img
   #  enhancer = ImageEnhance.Color(img)
    
   #  blackAndWhite = enhancer.enhance(0.0)
   #  print(blackAndWhite)
    import numpy as np
    arr = np.array(img)
    arr[arr < 170] = 0
    img = Image.fromarray(arr)
    blackAndWhite = img
    blackAndWhite = blackAndWhite.convert("L")
   #  blackAndWhite.show()
    wpercent = (300/float(blackAndWhite.size[0]))
    hsize = int((float(blackAndWhite.size[1])*float(wpercent)))
    blackAndWhite = blackAndWhite.resize((300,hsize), PIL.Image.ANTIALIAS)
    blackAndWhite.show()
    for x in range(blackAndWhite.width):
        for y in range(blackAndWhite.height):
            if blackAndWhite.getpixel( (x,y) )< 170: 
                # set to black
                blackAndWhite.putpixel( (x,y) ,0)
            else:
                # set to white
                blackAndWhite.putpixel( (x,y) ,255)

   #  blackAndWhite.show()


    #now iterating through each row, looking for letters



    #found letters

    foundletters = []

    for x in range(blackAndWhite.width):
        for y in range(blackAndWhite.height):
            if (x,y) not in foundAlready:
                if blackAndWhite.getpixel((x,y)) == 0: 
                    #reset letterlist, list for this individual 
                    
                    q = findSurrounding( (x,y), myletter( (x,y) ) )
                    foundletters.append(q)


    # print(foundletters)
    # look at found letters and make dict with order in frequences of bottom line
    # ycoord: [frequences, [rightest xcoords of that char]]

    myletterFrequences = {}
    for i in foundletters:
        # print(i.allPixels)
        left, right, base, high = i.findExtremes()
        # print(myletterFrequences)
        # print(base)

        if base in myletterFrequences:
            myletterFrequences[base] = [myletterFrequences[base][0] + 1, myletterFrequences[base][1] + [right] , myletterFrequences[base][2] + [left], myletterFrequences[base][3] + [high] ]
        else:
            myletterFrequences[base] = [1, [right], [left], [high]]

    # for i in myletterFrequences.values():
    #     print(len(i[1]))

    tolerance = 30

    # create new image to save the typed words to

    newImg = Image.new('RGB', (img.width, img.height), backColor) #(255, 255, 255)
    # newImg.show()
    wpercent = 1/ wpercent
    #copy paste to new doc
    # print(myletterFrequences)
    for k, v in myletterFrequences.items():
        # print(v[0])
        if v[0] < tolerance:
            #doesnt pass tolerance of frequences
            continue
        else:
            right = max(v[1])
            left = min(v[2])
            high = min(v[3])

            bufferhigh = (high - k) * 3
            bufferlow = (high - k) * 6
            # print(v[3])
            
            
            l = math.floor(left * wpercent)
            t = math.floor((high +  bufferhigh) * wpercent)
            r = math.ceil(right * wpercent)
            b = math.ceil((k - bufferlow) * wpercent)
            cut = img.crop( (l, t, r, b ))
            # raise ValueError()
            newImg.paste(cut, (l, t)) 
            # print('test')

    return(newImg)
    # newImg.save('after.jpg')



    



