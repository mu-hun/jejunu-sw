import numpy as np
import cv2

image = np.ones((200, 300), np.float64)  # 200x300 단색 영상 생성
image[:] = 100  # 밝기 값 100으로 변경

cv2.waitKey(0)  # 키 이벤트(key event) 대기
cv2.destroyAllWindows()
