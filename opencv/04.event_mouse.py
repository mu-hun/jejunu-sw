import numpy as np
import cv2

def onMouse(event, x, y, flags, param):                         # 콜백 함수 – 이벤트 내용 출력
    


image = np.full((200, 300), 255, np.uint8)



                    # 

title1, title2 = "Mouse Event1", "Mouse Event2"     #
cv2.imshow(title1, image) # 영상 보기
cv2.imshow(title2, image)

     	# 마우스 콜백 함수

cv2.waitKey(0)                                      # 
cv2.destroyAllWindows()                             # 
