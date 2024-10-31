import numpy as np, cv2

image1 = cv2.imread("Source/chap06/images/add1.jpg", cv2.IMREAD_GRAYSCALE)   # 영상 읽기
image2 = cv2.imread("Source/chap06/images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")

# 영상 합성







titles = [                                 ]
for t in titles: cv2.imshow(t, eval(t))
cv2.waitKey(0)
