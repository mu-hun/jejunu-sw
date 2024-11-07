import cv2


def onThreshold(value: int):
    result = cv2.threshold(image, value, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("result", result)


image = cv2.imread("chap06/images/color_space.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류")

cv2.namedWindow("result")
cv2.createTrackbar("threshold", "result", 128, 255, onThreshold)
cv2.imshow("image", image)
cv2.waitKey(0)
