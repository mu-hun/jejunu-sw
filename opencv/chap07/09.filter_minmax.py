import numpy as np, cv2

def minmax_filter(image, ksize, mode):
   




    return dst

image = cv2.imread("chap07/images/min_max.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
    



cv2.imshow("image", )
cv2.imshow("minfilter_img",)
cv2.imshow("maxfilter_img", )
cv2.waitKey(0)