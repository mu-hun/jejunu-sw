import numpy as np
import cv2

# numpy array이용해 단일 채널 3개 생성
ch0 = 
ch1 = 
ch2 = 

list_bgr =                       # 단일 채널들을 모아 리스트 구성
merge_bgr =               # 채널 합성
split_bgr =                # 채널 분리: 컬러영상--> 3채널 분리

print('split_bgr 행렬 형태 ', np.array(split_bgr).shape)
print('merge_bgr 행렬 형태', merge_bgr.shape)

print('라스트 행렬 형태', np.array())

print("[ch0] = \n%s" % )                     # 단일 채널 원소 출력
print("[ch1] = \n%s" % )
print("[ch2] = \n%s" % )
print("[merge_bgr] = \n %s\n" % )       # 다중 채널 원소 출력

print("[split_bgr[0]] =\n%s " % )
print("[split_bgr[1]] =\n%s " % )
print("[split_bgr[2]] =\n%s " % )