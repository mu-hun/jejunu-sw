import cv2
from Common.utils import cwd

# 시험에 내기 좋습니다!!

image = cv2.imread(cwd() / "images/color.jpg", cv2.IMREAD_COLOR)  # 영상 읽기
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")  # 예외 처리
if image.ndim != 3:
    raise Exception("컬러 영상 아님")

bgr = cv2.split(image)  # 채널 분리: 컬러영상--> 3채널 분리
# blue, green, red = cv2.split(image)

print("bgr 자료형:", type())
print("bgr 원소개수:", len(bgr))

# 각 채널을 윈도우에 띄우기
cv2.imshow("image", image)


cv2.waitKey()
