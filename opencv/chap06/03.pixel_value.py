import cv2

image = cv2.imread("chap06/images/pixel.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")


print("[roi_img] =")

for row in roi_img:
    for p in row:
    print("%4d" % p, end="")

cv2.
cv2.imshow("image", image)
cv2.waitKey(0)
