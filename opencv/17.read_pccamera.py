import cv2


def put_string(
    frame, text, pt, value, color=(120, 200, 90)
):  # 문자열 출력 함수 - 그림자 효과
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)  # 그림자 효과
    cv2.putText(frame, text, pt, font, 0.7, (120, 200, 90), 2)  # 글자 적기


capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

# 카메라 속성 획득 및 출력
print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))

while True:
    ret, frame = capture.read()
    if not ret:
        break

    put_string(frame, "EXPOS:", (10, 40), capture.get(cv2.CAP_PROP_EXPOSURE))

    title = "View Frame from Camera"
    cv2.imshow(title, frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # 'q' 키를 누르면 종료
        break
capture.release()
cv2.destroyAllWindows()
