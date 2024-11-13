import numpy as np, cv2
from  Common.filters import filter

def differential(image, data1, data2):
    mask1 = 
    mask2 = 

    dst1 = 
    dst2 = 
    dst = 

    dst = 
    
    dst1 =  
    dst2 = 
    return dst, dst1, dst2

image = cv2.imread("chap07/images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = []
data2 = []
dst, dst1, dst2 = differential(image, data1, data2)

cv2.imshow("image", )
cv2.imshow("prewitt edge", )
cv2.imshow("dst1 - vertical mask", )
cv2.imshow("dst2 - horizontal mask", )
cv2.waitKey(0)