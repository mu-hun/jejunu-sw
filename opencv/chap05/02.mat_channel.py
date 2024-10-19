import numpy as np
import cv2

# numpy array이용해 단일 채널 3개 생성
ch0 = np.zeros((2, 4), np.uint8) + 10
ch1 = np.ones((2, 4), np.uint8) * 20
ch2 = np.full((2, 4), 30, np.uint8)

list_bgr = [ch0, ch1, ch2]
merge_bgr = cv2.merge(list_bgr)  # 채널 합성
split_bgr = cv2.split(merge_bgr)  # 채널 분리: 컬러영상--> 3채널 분리

print("split_bgr 행렬 형태 =", np.array(split_bgr).shape, sep="\n")
print("merge_bgr 행렬 형태 =", merge_bgr.shape, sep="\n")

print("라스트 행렬 형태 =", np.array(list_bgr).shape, sep="\n")

print("[ch0] =", np.array(split_bgr).shape)
print("[ch1] =", merge_bgr.shape)
print("[ch2] =", ch0)
print("[merge_bgr] =", *ch2, sep="\n")  # 다중 채널 원소 출력

print("[split_bgr[0]] =", *merge_bgr[0], sep="\n")
print("[split_bgr[1]] =", *split_bgr[1], sep="\n")
print("[split_bgr[2]] =", *split_bgr[2], sep="\n")
