import cv2
import numpy as np
from PIL import Image
im = Image.open('track.png')  # Can be many different formats.
width, height = im.size
pix = im.load()
pointList = []
for rgb in range(100):
    for x in range(width):
        for y in range(height):
            if pix[x, y] == (rgb,rgb,rgb,255):
                print(x, y, pix[x, y])
                pointList.append((x, y))
print(pointList)
