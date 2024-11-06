import cv2
import numpy as np

image = cv2.imread("chap05/images/color.jpg", cv2.IMREAD_COLOR)  # 영상 읽기
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")  # 예외 처리

mask = np.zeros(image.shape[:2], dtype=np.uint8)  # 마스크 생성
center = (190, 170)  # 마스크의 중심 좌표

cv2.ellipse(image, center, (100, 50), 90, 0, 360, 255, -1)  # 마스크에 타원 그리기

# 타원 영역의 이미지를 복사
masked_image = cv2.bitwise_and(image, image, mask=mask)

# 각 채널을 윈도우에 띄우기
cv2.imshow("masked_image", masked_image)
# 각 채널을 윈도우에 띄우기
cv2.imshow("image", image)

cv2.waitKey()
