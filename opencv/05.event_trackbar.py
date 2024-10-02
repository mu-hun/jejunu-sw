import numpy as np
import cv2

def onChange(value):												# 트랙바 콜백 함수
    global image                        	# 전역 변수 참조

                	
    cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8)           	# 영상 생성

title = 'Trackbar Event'
cv2.imshow(title, image)

cv2.	# 트랙바 콜백 함수 등록
cv2.waitKey(0)
cv2.destroyWindow(title)