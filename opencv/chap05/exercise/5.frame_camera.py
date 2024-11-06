import cv2
import numpy as np

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # 메인 윈도우 크기 설정 400x300
    frame = cv2.resize(frame, (400, 300))

    roi = {
        "x": 30,
        "y": 30,
        "width": 320,
        "height": 240,
    }

    # 선택 영역을 슬라이싱하여 selected_area 변수에 할당
    selected_area = frame[
        roi["x"] : roi["y"] + roi["height"], roi["x"] : roi["x"] + roi["width"]
    ]

    # 선택 영역에 빨간색 테두리 추가
    cv2.rectangle(
        frame,
        (roi["x"], roi["y"]),
        (roi["x"] + roi["width"], roi["y"] + roi["height"]),
        (0, 0, 255),
        2,
    )

    # 검정 배경으로 마스크 생성
    mask = np.zeros_like(frame)
    # 선택 영역 영상 selected_area 을 생성한 마스크에 할당
    mask[roi["y"] : roi["y"] + roi["height"], roi["x"] : roi["x"] + roi["width"]] = (
        selected_area
    )
    # 마스크 영상을 윈도우에 표시
    cv2.imshow("View Frame from Camera", mask)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # 'q' 키를 누르면 종료
        break
capture.release()
cv2.destroyAllWindows()
