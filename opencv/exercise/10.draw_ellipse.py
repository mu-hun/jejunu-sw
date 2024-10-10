import numpy as np, cv2


def onMouse(event, x, y, flags, param):
    global title, pt
    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)
    elif event == cv2.EVENT_MBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
            return
        dx, dy = pt[0] - x, pt[1] - y
        radius = int(np.sqrt(dx * dx + dy * dy))
        cv2.ellipse(image, pt, (radius * 2, radius), 0, 0, 360, (0, 255, 0), 3)
        cv2.imshow(title, image)
        pt = (-1, -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx * dx + dy * dy))
            cv2.circle(image, pt, radius, (0, 0, 255), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)


pt = (-1, -1)
title = "Draw Event"
image = np.ones((300, 300), np.uint8) * 255

cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
