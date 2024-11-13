import cv2

def onTrackbar(th):																	# 트랙바 콜백 함수
	
	cv2.imshow("Canny", rep_edge)

	h, w = image.shape[:2]
	
	cv2.imshow("color edge", color_edge)

image = cv2.imread("chap07/images/color_edge.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

th = 50
rep_image = 
rep_gray = 


cv2.imshow("rep_image", )
cv2.namedWindow("color edge", )    		# 윈도우 생성
cv2.createTrackbar("Canny th", "color edge", )	# 콜백 함수 등록
onTrackbar(th)																					# 콜백 함수 첫 실행
cv2.waitKey(0)