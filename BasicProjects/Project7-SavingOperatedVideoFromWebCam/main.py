import cv2 as cv

import numpy as np

capture=cv.VideoCapture(0)

FourCC=cv.VideoWriter_fourcc(*'XVID')

out=cv.VideoWriter('output.avi',FourCC,20.0,(640,480))


#run a loop to read frames from Camera

while(True):
    ret,frame=capture.read()

    out.write(frame)

    cv.imshow('live',frame)

    if(cv.waitKey(1) & 0xFF==ord('a')):
        break

capture.release()

out.release()

cv.destroyAllWindows()