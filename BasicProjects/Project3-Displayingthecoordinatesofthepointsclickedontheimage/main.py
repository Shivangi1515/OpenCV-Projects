import cv2 as cv

# [print(i) for i in dir(cv) if 'EVENT' in i]

def click_event(event,x,y,flags,params):
    if event==cv.EVENT_LBUTTONDOWN:
        print(x," ",y)
        font=cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img,str(x)+','+str(y),(x,y),font,1,(255,0,0),2)
        cv.imshow('image',img)

    if event==cv.EVENT_RBUTTONDOWN:
        print(x," ",y)
        font=cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img,str(x)+','+str(y),(x,y),font,1,(255,0,0),2)
        cv.imshow('image',img)

if __name__=="__main__":
    img=cv.imread("BasicProjects\Project3-Displayingthecoordinatesofthepointsclickedontheimage\Cat2.jpg",1)

    cv.imshow('image',img)

    cv.setMouseCallback('image',click_event)

    cv.waitKey(0)
    cv.destroyAllWindows()


