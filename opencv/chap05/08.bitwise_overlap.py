import numpy as np, cv2

image = cv2.imread("Source/chap05/images/bit_test.jpg", cv2.IMREAD_COLOR)     # 원본 영상 읽기
logo  = cv2.imread("Source/chap05/images/logo.jpg", cv2.IMREAD_COLOR)         # 로고 영상 읽기
if image is None or logo is None: raise Exception("영상 파일 읽기 오류 ")

masks = cv2.threshold()  # 로고 영상 이진화
masks = cv2.split(masks)

fg_pass_mask = 
fg_pass_mask = 
bg_pass_mask = 

cv2.imshow("masks[0]", masks[0]);
cv2.imshow("masks[1]", masks[1]);
cv2.imshow("masks[2]", masks[2]);

cv2.imshow("fg_pass_mask", fg_pass_mask);




# 행렬 논리곱과 마스킹을 이용한 관심 영역 복사
foreground = 
background = 

dst = 
image[y:y+h, x:x+w] = dst             # 합성 영상을 원본에 복사

cv2.imshow("background", background);  cv2.imshow("forground", foreground)
cv2.imshow("dst", dst);                 cv2.imshow("image", image)
cv2.waitKey()