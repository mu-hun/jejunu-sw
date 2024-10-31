import numpy as np, cv2

image1 = np.zeros((50, 512), np.uint8)
image2 = np.zeros((50, 512), np.uint8)

rows, cols = image1.shape[:2]

for i in range(rows):  # 행렬 전체 조회
    for j in range(cols):
        image1[i, j] = j % 256
        # AttributeError: `itemset` was removed from the ndarray class in NumPy 2.0. Use `arr[index] = value` instead.
        # image1.itemset((i, j), j % 256)
        image2[i, j] = j // 2
        # image2.itemset((i, j), j // 2)


cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.waitKey(0)
