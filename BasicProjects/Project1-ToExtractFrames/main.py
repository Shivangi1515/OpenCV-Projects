import cv2 as cv

def FrameCapture(path):
    vidobj=cv.VideoCapture(path)
    count=0
    success=1  #used whether frame extracted or not
    while success:

        success,image=vidobj.read()
        cv.imwrite("Frame%d.jpg" % count,image)
        count+=1




if __name__=='__main__':
    FrameCapture(r"BasicProjects/Project1-ToExtractFrames/video/video1.mp4")