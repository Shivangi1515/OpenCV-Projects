import cv2 as cv

import argparse  #handle commandline arguments

ref_point=[] #stores starting and ending point of the rectangle

crop=False

def shape_selection(event,x,y,flags,params):
    global ref_point,crop

    if event==cv.EVENT_LBUTTONDOWN:
        ref_point=[(x,y)]

    elif event==cv.EVENT_LBUTTONUP:
        ref_point.append((x,y))

        cv.rectangle(image,ref_point[0],ref_point[1],(0,255,0),2)
        cv.imshow("image",image)

ap=argparse.ArgumentParser()

ap.add_argument("-i","--image",required=True,help="Path to image")

args=vars(ap.parse_args())

image=cv.imread(args["image"])

clone=image.copy()
cv.namedWindow("image")

cv.setMouseCallback("image",shape_selection)

while True:
    cv.imshow("image",image)
    key=cv.waitKey(1) & 0xFF

    if key==ord("r"):
        image=clone.copy()

    elif key==ord("c"):
        break

if len(ref_point)==2: #Here 2 represents the starting and ending point of rectangle
    crop_img=clone[ref_point[0][1]:ref_point[1][1],ref_point[0][0]:ref_point[1][0]]
    cv.imshow("cropimage",crop_img)
    cv.waitKey(0)


cv.destroyAllWindows()




