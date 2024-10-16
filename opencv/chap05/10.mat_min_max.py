import numpy as np, cv2

data = [10, 200, 5 , 7 ,  9,
        15, 35 , 60, 80, 170,
        100, 2 , 55, 37, 70]
m1 = 
m2 = 

m_min = 
m_max = 

## 행렬의 최솟값/최댓값과 그 좌표들을 반환
 = cv2.minMaxLoc(m1)

print("[m1] = \n%s\n" % m1)
print("[m_min] = \n%s\n" % m_min)
print("[m_max] = \n%s\n" % m_max)

# min_loc와 max_loc 좌표는 (y, x)이므로 행렬의 좌표 위차와 반대임
print("m1 행렬 최솟값 좌표 %s, 최솟값: %d" %(min_loc, min_val) )
print("m1 행렬 최댓값 좌표 %s, 최댓값: %d" %(max_loc, max_val) )