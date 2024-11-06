import cv2


def adjust_brightness(image, x, y, width, height, value):
    roi = image[y : y + height, x : x + width]
    # 관심 영역에 value 만큼 밝게 처리
    adjusted_roi = cv2.add(roi, value)
    image[y : y + height, x : x + width] = adjusted_roi


def adjust_contrast(image, x, y, width, height, alpha):
    roi = image[y : y + height, x : x + width]
    # 관심 영역에 alpha 만큼 대비 증가 처리
    adjusted_roi = cv2.addWeighted(roi, alpha, roi, 0, 0)
    image[y : y + height, x : x + width] = adjusted_roi


image = cv2.imread("chap05/images/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

# 관심 영역 1 설정 및 50만큼 밝게 처리
adjust_brightness(image, 0, 0, 100, 100, 50)

# 관심 영역 2 설정 및 2만큼 대비 증가 처리
adjust_contrast(image, 100, 100, 100, 100, 2)

# 윈도우에 이미지 표시
cv2.imshow("", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
