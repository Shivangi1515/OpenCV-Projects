import cv2 as cv

import numpy as np

def emptyFunction():
    pass

image=np.zeros((512,512,3),np.uint8)

windowName="OpenCV color Palette"

cv.namedWindow(windowName)

cv.createTrackbar('Blue',windowName,0,255,emptyFunction)
cv.createTrackbar('Green',windowName,0,255,emptyFunction)
cv.createTrackbar('Red',windowName,0,255,emptyFunction)

while(True):
    cv.imshow(windowName,image)
    if cv.waitKey(1)==27: #ascii code for esc key
        break
    blue=cv.getTrackbarPos('Blue',windowName)
    green=cv.getTrackbarPos('Green',windowName)
    red=cv.getTrackbarPos('Red',windowName)

    image[:]=[blue,green,red]

    print(blue,green,red)
    