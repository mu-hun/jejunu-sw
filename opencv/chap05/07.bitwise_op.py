import numpy as np, cv2

image1 = np.zeros((300, 300), np.uint8)     		# 300행, 300열 검은색 영상 생성
image2 = image1.copy()






cv2.imshow("image1", image1);			cv2.imshow("image2", image2)
cv2.imshow("bitwise_or", image3);		cv2.imshow("bitwise_and", image4)
cv2.imshow("bitwise_xor", image5);	cv2.imshow("bitwise_not", image6)
cv2.waitKey(0)