import cv2

image = cv2.imread("Source/chap06/images/bright.jpg", cv2.IMREAD_GRAYSCALE)    # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

# OpenCV 함수 이용








cv2.imshow("original image", )
cv2.imshow("     ", )
cv2.imshow("     ", )
cv2.imshow("       ", )
cv2.imshow("        ", );
cv2.waitKey(0)