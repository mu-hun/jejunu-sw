import cv2
import numpy as np

image = cv2.imread("chap06/images/bright.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None:
    raise Exception("영상 파일 읽기 오류")

src2 = np.full(
    image.shape, 100, dtype=image.dtype
)  # 100 원시 값을 그대로 할당해도 되나, mypy 타입 검사를 위해 dtype 지정함

dst1 = cv2.add(image, src2)  # 밝기 증가
dst1 = cv2.add(image, src2)  # 밝기 증가
dst2 = cv2.subtract(image, src2)  # 밝기 감소

# numpy.ndarray 이용 (modulo 연산)
dst3 = image + 100  # 밝기 증가
dst4 = image - 100  # 밝기 감소


cv2.imshow("original image", image)
cv2.imshow("cv: bright image1", dst1)
cv2.imshow("cv: bright image2", dst2)
cv2.imshow("np: bright image3", dst3)
cv2.imshow("np: bright image4", dst4)

cv2.waitKey(0)
