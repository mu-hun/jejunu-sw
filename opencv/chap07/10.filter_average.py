import numpy as np, cv2

image = cv2.imread("Source/chap07/images/filter_avg.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")





cv2.imshow("image", ),
cv2.imshow("blur_img", )
cv2.imshow("box_img", )
cv2.waitKey(0)