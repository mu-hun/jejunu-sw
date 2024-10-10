import cv2


capture = cv2.VideoCapture(2)  # 0번 카메라 연결
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")
fps = 15  # 초당 프레임 수
delay = round(1000 / fps)  # 프레임 간 지연 시간 계산
size = (640, 480)  # 해상도
fourcc = cv2.VideoWriter.fourcc(*"DIVX")  # 인코딩 포맷 문자

print("width x height: ", size)
print("VideoWriter_fourcc: ", fourcc)
print("delay: %d ms" % delay)
print("fps: %d" % fps)

capture.set(cv2.CAP_PROP_ZOOM, 1)
capture.set(cv2.CAP_PROP_FOCUS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

writer = cv2.VideoWriter("images/output/Flip_test.avi", fourcc, fps, size)

if writer.isOpened() == False:
    raise Exception("동영상 파일 개방 안됨")

while True:
    ret, frame = capture.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    writer.write(frame)
    cv2.imshow("View Frame from Camera", frame)
    if cv2.waitKey(delay) == 27:  # ESC로 종료
        break

writer.release()
capture.release()
cv2.destroyAllWindows()
