import numpy as np, cv2
from Common.filters import erode, dilate

def opening(img, mask):                     # 열림 연산
    
    return dst

def closing(img, mask):                     # 닫힘 연산
   
    return dst

image = cv2.imread("chap07/images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.array([[0, 1, 0],                 # 마스크 초기화
                 [1, 1, 1], 
                 [0, 1, 0]]).astype("uint8")
th_img = 

dst1 = 
dst2 = 
dst3 = 
dst4 = 

cv2.imshow("User opening", dst1);       cv2.imshow("User closing", dst2)
cv2.imshow("OpenCV opening", dst3);     cv2.imshow("OpenCV closing", dst4)
cv2.waitKey(0)