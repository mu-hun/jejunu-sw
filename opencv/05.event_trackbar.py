import numpy as np
import cv2


def onChange(value):
    global image
    image += value - int(image[0][0])

    cv2.imshow(title, image)


image = np.zeros((300, 500), np.uint8)  # 영상 생성

title = "Trackbar Event"
cv2.imshow(title, image)

cv2.createTrackbar("name", title, 0, 255, onChange)  # 트랙바 콜백 함수 등록
cv2.waitKey(0)
cv2.destroyAllWindows()
