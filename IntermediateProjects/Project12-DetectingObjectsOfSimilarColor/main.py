#Color segmentation Based Object Tracking
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cap=cv.VideoCapture(0)

def nothing(x): #this empty function used to create trackbars

    pass

cv.namedWindow('Tracking')

cv.createTrackbar('LH',"Tracking",0,255,nothing)
cv.createTrackbar('LS',"Tracking",0,255,nothing)
cv.createTrackbar('LV',"Tracking",0,255,nothing)
cv.createTrackbar('HH',"Tracking",0,255,nothing)
cv.createTrackbar('HS',"Tracking",0,255,nothing)
cv.createTrackbar('HV',"Tracking",0,255,nothing)

#Loop to continuosuly process the video frame

while True:
    b,frame=cap.read()
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    l_h=cv.getTrackbarPos("LH","Tracking")
    l_s=cv.getTrackbarPos("LS","Tracking")
    l_v=cv.getTrackbarPos("LV","Tracking")
    h_h=cv.getTrackbarPos("HH","Tracking")
    h_s=cv.getTrackbarPos("HS","Tracking")
    h_v=cv.getTrackbarPos("HV","Tracking")

    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([h_h,h_s,h_v])

    mask=cv.inRange(hsv,l_b,u_b) #converts into binary image
    res=cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow('Frame',frame)
    cv.imshow('Mask',mask)
    cv.imshow('res',res)

    if cv.waitKey(25) and 0Xff==ord('r'):
        break
cv.release()
cv.destroyAllWindows()

