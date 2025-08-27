import cv2 as cv

img=cv.imread('BasicProjects\Project9-CartooningAnImage\salmankhan.jpeg')

color=cv.bilateralFilter(img,d=9,sigmaColor=75,sigmaSpace=75) #sigmaColor-->determines how color in neighbourhood pixel mix  & sigmaSpace-->determines extent of the area around each pixel

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray_blur=cv.medianBlur(gray,7)

edges=cv.adaptiveThreshold(gray_blur,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,9,9)

cartoon=cv.bitwise_and(color,color,mask=edges)

cv.imshow('Cartoonised image',cartoon)

cv.waitKey(0)

cv.destroyAllWindows()
