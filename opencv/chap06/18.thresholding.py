import cv2

def onThreshold(value):
    
    cv2.imshow("result", result)


image = cv2.imread("Source/chap06/images/color_space.jpg", cv2.IMREAD_GRAYSCALE) # 컬러 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

cv2.namedWindow("result")



cv2.imshow("image", image)
cv2.waitKey(0)