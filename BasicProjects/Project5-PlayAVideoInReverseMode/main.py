import cv2 as cv

capture=cv.VideoCapture("BasicProjects/Project5-PlayAVideoInReverseMode/video1.mp4")

check,vid=capture.read()

counter=0 #to count frames

frame_list=[]

# to capture and save the frames

while(check==True):
    cv.imwrite("frame%d.jpg" % counter,vid)
    check,vid=capture.read()
    frame_list.append(vid)
    counter+=1

frame_list.pop() #to remove none value

frame_list.reverse()

for frame in frame_list:
    cv.imshow("Frame",frame)
    if cv.waitKey(25) and 0xff==ord('q'):
        break
capture.release()
cv.destroyAllWindows()




