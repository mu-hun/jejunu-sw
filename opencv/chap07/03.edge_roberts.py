import numpy as np, cv2
from  Common.filters import filter

def differential(image, data1, data2):
    

    
    return dst, dst1, dst2

image = cv2.imread("Source/chap07/images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
     
data1 = []
data2 = []
dst, dst1, dst2 =  		# 회선 수행 및 두 방향의 크기 계산

cv2.imshow("image", )
cv2.imshow("roberts edge", )
cv2.imshow("dst1", )
cv2.imshow("dst2", )
cv2.waitKey(0)