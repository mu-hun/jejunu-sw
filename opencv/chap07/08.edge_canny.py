import numpy as np, cv2

image = cv2.imread("Source/chap07/images/canny.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")


             # OpenCV 캐니 에지

cv2.imshow("image", )
cv2.imshow("OpenCV_Canny", )           # OpenCV 캐니 에지
cv2.waitKey(0) 