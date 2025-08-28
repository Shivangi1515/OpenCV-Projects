import cv2 as cv

import pytesseract  #for character or text detection

pytesseract.pytesseract.tesseract_cmd=r"C:/Program Files/Tesseract-OCR/tesseract.exe"

img=cv.imread("IntermediateProjects/Project10-TextDetectionAndExtraction/image.jpeg")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#extracting text from image

text=pytesseract.image_to_string(gray)

print(text)

# cv.imshow("Demo",gray)

# cv.waitKey(0)