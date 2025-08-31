#Template Matching is a Method for searching and finding the location of template image in a Larger Image

import cv2 as cv
import numpy as np

img=cv.imread('IntermediateProjects/Project10-TextDetectionAndExtraction/Project11-TemplateMatching/img.jpg',0)
# template=cv.imread('IntermediateProjects/Project10-TextDetectionAndExtraction/Project11-TemplateMatching/football.jpg',0)
template=cv.imread('IntermediateProjects/Project10-TextDetectionAndExtraction/Project11-TemplateMatching/Left_leg.jpg',0)

h,w=template.shape  #get height and width of template image

methods=[cv.TM_CCOEFF,cv.TM_CCOEFF_NORMED,cv.TM_CCORR,cv.TM_CCORR_NORMED,cv.TM_SQDIFF,cv.TM_SQDIFF_NORMED]

for method in methods:
    img2=img.copy()
    result=cv.matchTemplate(img2,template,method)
    min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)

    if method in [cv.TM_SQDIFF,cv.TM_SQDIFF_NORMED]:
        location=min_loc
    else:
        location=max_loc
    bottom_right=(location[0]+w,location[1]+h)
    cv.rectangle(img2,location,bottom_right,255,5)
    cv.imshow('Match',img2)
    cv.waitKey(0)
    cv.destroyAllWindows()


