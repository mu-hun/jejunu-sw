import numpy as np, cv2

def erode(img, mask=None):
    dst = np.zeros(img.shape, np.uint8)
    

    mcnt = cv2.
    for i in range(ycenter, img.shape[0] - ycenter):           # 입력 행렬 반복 순회
        for j in range(xcenter, img.shape[1] - xcenter):
            
            dst[i, j] = 255 if (cnt == mcnt) else 0            # 출력 화소에 저장
    return dst

image = cv2.imread("chap07/images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data = [0, 1, 0,                                               # 마스크 선언 및 초기화
        1, 1, 1,
        0, 1, 0]
mask = 
th_img = 

dst1 = 
dst2 = 

cv2.imshow("image", )
cv2.imshow("binary image", )
cv2.imshow("User erode", )
cv2.imshow("OpenCV erode", )
cv2.waitKey(0)