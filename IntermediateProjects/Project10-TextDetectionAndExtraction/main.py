# Text Detection and Extraction using OpenCV and OCR

import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'tesseract'

img = cv.imread("IntermediateProjects/Project10-TextDetectionAndExtraction/sample.jpeg")

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)
print(text)

file = open("recognized.txt","w+")
file.write(text)
file.close()

# cv.imshow("Demo",gray)
# cv.waitKey(0)