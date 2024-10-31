import numpy as np, cv2

def calc_histo(image, hsize, ranges=[0, 256]):  # 행렬 원소의 1차원 히스토그램 계산
    



    return hist

image = cv2.imread("Source/chap06/images/pixel.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")

hsize, ranges =
gap = 





print("User 함수: \n", )                # 
print("OpenCV 함수: \n",)                # 
print("numpy 함수: \n", )                           # 

cv2.imshow("image", image)
cv2.waitKey(0)