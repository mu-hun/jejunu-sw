import numpy as np
import cv2

def onChange(value):
    global image, title                                 # 전역 변수 참조

    add_value = value - int(image[0][0])                # 트렉바 값과 영상화소값 차분
    
    cv2.imshow(title, image)

def onMouse(event, x, y, flags, param):                 # 마우스 콜백 함수
    global image, bar_name
    
    if event == cv2.EVENT_RBUTTONDOWN:
        print(image[0][0])
        
        
        		# 트랙바 위치 변경 
        cv2.imshow(title, image)
        
    elif event == cv2.EVENT_LBUTTONDOWN :
       
       		# 트랙바 위치 변경 
        cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8)                 

title = "Trackbar & Mouse Event"                    		# 윈도우 이름
bar_name = "Brightness"                                # 트랙바 이름
cv2.imshow(title, image)    

cv2.                           # 트랙바 콜백 함수
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)													# 키 입력 대기
cv2.destroyAllWindows()                                	# 모든 윈도우 닫기