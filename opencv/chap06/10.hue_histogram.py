import numpy as np, cv2

def make_palette(rows):
    # 리스트 생성 방식
   

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)         


def draw_histo_hue(hist, shape=(200, 256,3)):
    
    gap = hist_img.shape[1] / hist.shape[0]  # 한 계급 크기
    for i, h in enumerate(hist):
       


    return cv2.flip(hist_img, 0)

image = cv2.imread("chap06/images/hue_hist.jpg", cv2.IMREAD_COLOR)  # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

hsv_img = 
hue_hist = 
hue_hist_img =

cv2.imshow("image", )
cv2.imshow("hue_hist_img", )
cv2.waitKey(0)