import numpy as np, cv2

def dilate(img, mask):
    dst = np.zeros(img.shape, np.uint8)
    
    for i in range(ycenter, img.shape[0] - ycenter):    # 입력 행렬 반복 순회
        for j in range(xcenter, img.shape[1] - xcenter):
            
    return dst

image = cv2.imread("chap07/images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.array([[0, 1, 0],                         # 마스크 초기화
                 [1, 1, 1],
                 [0, 1, 0]]).astype("uint8")
th_img = 
dst1 = 
dst2 = 

cv2.imshow("User dilate", )
cv2.imshow("OpenCV dilate", )
cv2.waitKey(0)