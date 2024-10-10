import numpy as np
import cv2

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image = np.zeros((400, 600, 3), np.uint8)  # 영상 생성
image[:] = (255, 255, 255)  # 흰색으로 초기화

pt1, pt2 = (50, 130), (200, 300)

# 직선 그리기
cv2.line(image, pt1, (100, 200), blue)
cv2.line(image, pt2, (100, 100), green)

# 사각형 그리기
cv2.rectangle(image, pt1, pt2, (255, 0, 255))
cv2.rectangle(image, pt1, pt2, (0, 0, 255))

cv2.imshow("Line & Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
