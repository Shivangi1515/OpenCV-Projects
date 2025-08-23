#White and Black Dot Detection
import cv2 as cv

#path="BasicProjects/Project2-WhiteandBlackDotDetection/black-dot1.jpg"
path="BasicProjects\Project2-WhiteandBlackDotDetection\white-dot.png"

gray=cv.imread(path,0)

#threshold

#th,thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU) #for counting black dots
th,thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY|cv.THRESH_OTSU)

#findContours

cnts=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)[-2]

#filter by area

s1=3
s2=20
xcnts=[]

for cnt in cnts:
    if s1<cv.contourArea(cnt)<s2:
        xcnts.append(cnt)

# print(f"Total Number of Black Dot is{len(xcnts)}")
print(f"Total Number of white Dot is{len(xcnts)}")
