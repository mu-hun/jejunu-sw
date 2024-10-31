import numpy as np, cv2

def draw_histo(hist, shape=(200, 256)):
  
   

    for i, h in enumerate(hist):
        
    return   cv2.flip(hist_img, 0)                        # 영상 상하 뒤집기 후 반환

image = cv2.imread("Source/chap06/images/draw_hist.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")
    
hist = 
hist_img =

cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)
cv2.waitKey(0)