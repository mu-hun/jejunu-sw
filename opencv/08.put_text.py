import numpy as np
import cv2

olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165)
pt1, pt2 = (50, 200), (50, 260)                         # 문자열 위치 좌표

image = np.zeros((300, 500, 3), np.uint8)
image.fill(255)

cv2.putText(                    )
cv2.putText(                    )
cv2.putText(                             )
fontFace = cv2.FONT_HERSHEY_PLAIN | cv2.          # 
cv2.putText( )

cv2.imshow("Put Text", image)
cv2.waitKey(0)                                  # 