import numpy as np, cv2
from Common.histogram import draw_histo

def search_value_idx(hist, bias = 0):
    for i in range(hist.shape[0]):
    
    return -1                                   


image = cv2.imread("chap06/images/hist_stretch.jpg", cv2.IMREAD_GRAYSCALE)   # 영상읽기
if image is None: raise Exception("영상 파일 읽기 오류")

bsize, ranges = 
hist = 

bin_width  = 
high = 
low  = 

idx = 
idx =



dst = idx.astype('uint8')[image]



hist_dst = 
hist_img = 
hist_dst_img = 

print("high_value = ", high)
print("low_value = " , low)
cv2.imshow("image", image);         cv2.imshow("hist_img", hist_img)
cv2.imshow("dst", dst);             cv2.imshow("hist_dst_img", hist_dst_img)
cv2.waitKey(0)