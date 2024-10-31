import numpy as np, cv2

def calc_histo(image, hsize, ranges=[0, 256]): 
   
    
    for row in image: 
       

    return hist

def calc_histo2(image, hsize, ranges=[0, 256]):  
    

    idxs = 
    
    for i in idxs:
      

    return hist


image = cv2.imread("Source/chap06/images/pixel.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")

th_img =
cv2.imshow("th_img", th_img)
hsize, ranges = 
hist = 

print("사용자 정의 함수: \n",)  
cv2.imshow("image", )
cv2.waitKey(0)