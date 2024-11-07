import numpy as np, cv2

BGR_img = cv2.imread(
    "chap06/images/color_model.jpg", cv2.IMREAD_COLOR
)  # 컬러 영상 읽기
if BGR_img is None:
    raise Exception("영상 파일 읽기 오류")

white = np.array((255, 255, 255), np.uint8)  # 흰색 값 정의
CMY_img = (white - BGR_img).astype(np.uint8)  # CMY 색상 공간 계산
CMY = cv2.split(CMY_img)  # CMY 채널 분리

black = cv2.min(CMY[0], cv2.min(*CMY[1:]))  # CMY 채널 중 최소값 계산
yellow, magenta, cyan = CMY - black


titles = ["CMY_img", "black", "yellow", "magenta", "cyan"]
[cv2.imshow(t, eval(t)) for t in titles]
cv2.waitKey(0)
