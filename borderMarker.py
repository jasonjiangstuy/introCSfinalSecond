import PIL
from PIL import Image
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
import numpy as np
import math

# marker color
value = 0.5

tolerance = 

import numpy as np
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    array[idx]
    return array[idx]

img = Image.open(fileObj)
array = np.array(img)
print(array)
# [ 0.21069679  0.61290182  0.63425412  0.84635244  0.91599191  0.00213826
#   0.17104965  0.56874386  0.57319379  0.28719469]


cornerPx = find_nearest(array, value)
print(cornerPx)


# 0.568743859261




getMarker('testImgWithMarkers/difficult.jpg')
# returns image rotated perfectly