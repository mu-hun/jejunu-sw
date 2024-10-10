import cv2
import numpy as np

from typing import Literal

image = np.zeros((300, 500), np.uint8)
title = "create objects"


def create_circle(x: int, y: int):
    global image

    cv2.circle(image, (x, y), 20, (255, 255, 255), cv2.BORDER_DEFAULT)
    cv2.imshow(title, image)


def create_rectangle(x: int, y: int):
    global image

    cv2.rectangle(image, (x, y), (x + 20, y + 20), (255, 255, 255), cv2.BORDER_DEFAULT)
    cv2.imshow(title, image)


def onMouse(event: int, x: int, y: int, flags: int, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        create_circle(x, y)
    elif event == cv2.EVENT_RBUTTONDOWN:
        create_rectangle(x, y)


cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
