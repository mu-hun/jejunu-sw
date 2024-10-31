import numpy as np, cv2, time

def pixel_access1(image):
    image1 = 
    




    return image1

def pixel_access2(image):
    



    return image2

def pixel_access3(image):
    



    return image3

def pixel_access4(image):
    


    return image4

def pixel_access5(image):
   

   
    return image5

image = cv2.imread("Source/chap06/images/bright.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")

# 수행시간 체크
def time_check(func, msg):
    



    return ret_img

image1 = 
image2 = 
image3 = 
image4 = 
image5 = 

# 결과 영상 보기
cv2.imshow("image  - original", image)
cv2.imshow("image1 - directly access to pixel", image1)
cv2.imshow("image2 - item()/itemset()", image2)
cv2.imshow("image3 - LUT", image3)
cv2.imshow("image4 - OpenCV", image4)
cv2.imshow("image5 - ndarray 방식", image5)
cv2.waitKey(0)