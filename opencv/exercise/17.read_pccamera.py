import cv2
import numpy as np


capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

while True:
    ret, frame = capture.read()
    if not ret:
        break

    x, y, w, h = (200, 100, 100, 200)
    cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 3)

    blue, green, red = cv2.split(frame)
    tmp = green[y : y + h, x : x + w]
    cv2.add(tmp, 50, tmp)
    frame = cv2.merge((blue, green, red))

    title = "View Frame from Camera"
    cv2.imshow(title, frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # 'q' 키를 누르면 종료
        break
capture.release()
cv2.destroyAllWindows()
