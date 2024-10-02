import numpy as np
import cv2


def onMouse(event, x, y, flags, param):
    global title, pt  # 전역 변수 참조

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)  # 시작 좌표 지정
        else:
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)  # 시작 좌표 초기화

    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx * dx + dy * dy))
            cv2.circle(image, pt, radius, (0, 0, 255), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)


image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
