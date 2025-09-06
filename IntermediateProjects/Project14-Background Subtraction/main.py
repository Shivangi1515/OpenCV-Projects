#Background Subtraction Using OpenCV

"""
BackgroundSubtractorMOG:It is a Gaussian Mixture-Based background/Foreground Segmentation Algorithm

BackgroundSubtractorMOG2: It is also a Gaussian Mixrure-based Background-Foreground Segmentation Algorithm.It Provides Better Adaptability to varying scenee due illumination changes etc.

BackgroundSubtractorGMG: This algorithm combines statistical background image estimation and per-pixel Bayesian segmentation.
"""
import numpy as np
import cv2 as cv

fgbg1=cv.createBackgroundSubtractorMOG2()

cap=cv.VideoCapture(0)

while(1):
    ret,img=cap.read()

    fgmask1=fgbg1.apply(img)

    cv.imshow('Original',img)
    cv.imshow('MOG',fgmask1)
    k=cv.waitKey(30) & 0xff

    if k==27:  #esc key
        break
cap.release()
cv.destroyAllWindows()



