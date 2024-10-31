import numpy as np, cv2, math

def calc_hsi(bgr):
    
    return (H/2, S*255, I)

# BGR 컬러 -> HSI 컬러
def bgr2hsi(image):
    
    return (np.array(hsv)).astype('uint8')

BGR_img = cv2.imread("chap06/images/color_space.jpg", cv2.IMREAD_COLOR) # 컬러 영상 읽기
if BGR_img is None: raise Exception("영상 파일 읽기 오류")



titles = ['BGR_img','Hue','Saturation','Intensity']
[cv2.imshow(t, eval(t)) for t in titles]
[cv2.imshow('OpenCV_'+t, eval(t+'2')) for t in titles[1:]]	# OpenCV 결과 영상 표시
cv2.waitKey(0)