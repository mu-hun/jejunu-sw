import numpy as np
import cv2

image = np.ones((200, 300), np.float64)  # 200x300 단색 영상 생성

cv2.imshow("Keyboard Event", image)  # 윈도우에 영상 표시

cv2.waitKey(0)
cv2.destroyAllWindows()  # 열린 모든 윈도우 제거
