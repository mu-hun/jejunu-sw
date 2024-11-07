import cv2


window_name = "HSV & Hue Threshold"


def on_threshold_change(value):
    th1 = cv2.getTrackbarPos("Hue_th1", window_name)
    th2 = cv2.getTrackbarPos("Hue_th2", window_name)

    _, result = cv2.threshold(hue_channel, th2, 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(result, th1, 255, cv2.THRESH_BINARY, result)
    cv2.imshow(window_name, result)


BGR_img = cv2.imread("chap06/images/color_space.jpg", cv2.IMREAD_COLOR)
if BGR_img is None:
    raise Exception("Error reading image file")

HSV_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2HSV)

hue_channel = HSV_img[:, :, 0]

cv2.namedWindow(window_name)
cv2.createTrackbar("Hue_th1", window_name, 50, 255, on_threshold_change)
cv2.createTrackbar("Hue_th2", window_name, 100, 255, on_threshold_change)

cv2.imshow("BGR Image", BGR_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
