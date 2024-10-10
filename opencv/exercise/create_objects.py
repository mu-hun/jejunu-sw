import cv2
import numpy as np

from typing import Literal

image = np.zeros((300, 500), np.uint8)
title = "create objects"


def create_circle(x: int, y: int):
    global image

    cv2.circle(image, (x, y), 20, (255, 255, 255), circle_thickness)
    cv2.imshow(title, image)


def create_rectangle(x: int, y: int):
    global image

    cv2.rectangle(
        image,
        (x, y),
        (x + 20, y + 20),
        (255, 255, 255),
        rectangle_thickness,
    )
    cv2.imshow(title, image)


def onMouse(event: int, x: int, y: int, flags: int, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        create_circle(x, y)
    elif event == cv2.EVENT_RBUTTONDOWN:
        create_rectangle(x, y)


def onChange(type: str, value: int):
    global image, circle_thickness, rectangle_thickness
    if type == "circle":
        circle_thickness = value
    elif type == "rectangle":
        rectangle_thickness = value


cv2.imshow(title, image)

bar_name = "thickness"
cv2.setMouseCallback(title, onMouse)

circle_thickness = 1
rectangle_thickness = 1

cv2.createTrackbar(
    "rectangle",
    title,
    rectangle_thickness,
    10,
    lambda value: onChange("rectangle", value),
)
cv2.createTrackbar(
    "circle",
    title,
    circle_thickness,
    50,
    lambda value: onChange("circle", value),
)

cv2.waitKey(0)
cv2.destroyAllWindows()
