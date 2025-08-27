import cv2 as cv

img=cv.imread('BasicProjects/Project8-DrawingWithMouseOnImages/Cat2.jpg')

def draw_circle(event,x,y,flags,params):
    if event==cv.EVENT_LBUTTONDOWN:
        print("Hello")

        cv.circle(img,(x,y),100,(0,0,255),-1,2)

cv.namedWindow(winname="Popup Window")

cv.setMouseCallback("Popup Window",draw_circle)

while True:
    cv.imshow("Popup Window",img)
    if cv.waitKey(10) &  0xFF==27:
        break

cv.destroyAllWindows()




