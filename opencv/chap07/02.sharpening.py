import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("chap07/images/filter_sharpen.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

# 샤프닝 마스크 원소 지정 
data1 = 
data2 = 

mask1 = np.array(data2, np.float32)

 

cv2.imshow("image", image)
cv2.imshow("sharpen1", )  # 윈도우 표시 위한 형변환
cv2.imshow("sharpen2", )
cv2.waitKey(0)