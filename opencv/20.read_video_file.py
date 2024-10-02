import cv2
from Common.utils import put_string

capture = cv2.VideoCapture("images/move_file.avi")
if not capture.isOpened():
    raise Exception("동영상 파일 개방 안됨")  # 예외 처리

frame_rate = capture.get(cv2.CAP_PROP_FPS)  # 초당 프레임 수
delay = int(1000 / frame_rate)  # 지연 시간
frame_cnt = 0  # 현재 프레임 번호

while True:
    ret, frame = capture.read()
    if not ret or cv2.waitKey(delay) > 0:
        break
    blue, green, red = cv2.split(frame)  # 채널 분리
    frame_cnt += 1

    fixed_channel_value: cv2.typing.MatLike = 100  # type: ignore

    if 100 <= frame_cnt <= 200:
        cv2.add(blue, fixed_channel_value, blue)
    elif 200 < frame_cnt <= 300:
        cv2.add(green, fixed_channel_value, green)
    elif 300 < frame_cnt:
        cv2.add(red, fixed_channel_value, red)

    frame = cv2.merge((blue, green, red))  # 단일채널 영상 합성
    put_string(frame, "frame_cnt : ", (20, 320), frame_cnt)
    cv2.imshow("Read Video File", frame)

capture.release()
