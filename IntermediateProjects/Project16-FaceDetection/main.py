import cv2 as cv

a=cv.CascadeClassifier("IntermediateProjects/Project16-FaceDetection/haarcascade_frontalface_default.xml")  

#Haarcascade Frontal Face Detection is a pretrained classifier used to detect faces in images

cam=cv.VideoCapture(0) 

while True:
    ret,cam_img=cam.read()

    gray=cv.cvtColor(cam_img,cv.COLOR_BGR2GRAY)

    face=a.detectMultiScale(gray,1.3,6)

    for(x1,y1,w1,h1) in face:
        cv.rectangle(cam_img,(x1,y1),(x1+w1,y1+h1),(0,255,0),5)

    
    cv.imshow("Face",cam_img)
    if cv.waitKey(1) & 0xFF==ord('a'):
        break

cam.release()
cv.destroyAllWindows()