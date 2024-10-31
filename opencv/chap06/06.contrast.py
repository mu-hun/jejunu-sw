import numpy as np, cv2

image = cv2.imread("chap06/images/contrast.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")

noimage = 






# 영상 띄우기
cv2.imshow("image", )
cv2.imshow("dst1 - decrease contrast", )
cv2.imshow("dst2 - increase contrast", )
cv2.imshow("dst3 - decrease contrast using average", )
cv2.imshow("dst4 - increase contrast using average", )

cv2.imwrite("dst.jpg",)
cv2.waitKey(0)


