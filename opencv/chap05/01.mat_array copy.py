import cv2

image = cv2.imread("Source/chap05/images/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류 발생") # 예외 처리

x_axis =                  # x축 기준 상하 뒤집기
y_axis =                  # y축 기준 좌우 뒤집기
xy_axis = 
rep_image   =        # 반복 복사
trans_image =           # 행렬 전치

## 각 행렬을 영상으로 표시
titles = ['image', 'x_axis', 'y_axis','xy_axis','rep_image','trans_image']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)