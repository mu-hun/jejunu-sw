import numpy as np, cv2
from Common.histogram import draw_histo

image = cv2.imread("images/equalize.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")



# 히스토그램 누적합 계산




dst2 = 
hist1 = cv2.calcHist()   # 히스토그램 계산
hist2 = cv2.calcHist()   # 히스토그램 계산
hist_img = draw_histo()
hist_img1 = draw_histo()
hist_img2 = draw_histo()

cv2.imshow("image", image);             cv2.imshow("hist_img", hist_img)
cv2.imshow("dst1_User", dst1);          cv2.imshow("User_hist", hist_img1)
cv2.imshow("dst2_OpenCV", dst2);        cv2.imshow("OpenCV_hist", hist_img2)
cv2.waitKey(0)