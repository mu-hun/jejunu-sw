import numpy as np
import cv2

olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165)
pt1, pt2 = (50, 200), (50, 260)  # 문자열 위치 좌표

image = np.zeros((300, 500, 3), np.uint8)
image.fill(255)

cv2.putText(image, "SIMPLEX", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, olive)
cv2.putText(image, "DUPLEX", (50, 130), cv2.FONT_HERSHEY_DUPLEX, 3, violet)
cv2.putText(image, "TRIPLEX", pt1, cv2.FONT_HERSHEY_TRIPLEX, 4, brown)
fontFace = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC
cv2.putText(image, "ITALIC", pt2, fontFace, 4, brown)

cv2.imshow("Put Text", image)
cv2.waitKey(0)
