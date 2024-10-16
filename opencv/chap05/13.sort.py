import numpy as np, cv2
#from Common.utils import ck_time

#m = np.random.randint(0,100, 1000000).reshape(1000,1000)           # 임의 난수 생성
m = np.random.randint(0,100, 15).reshape(3,5)           # 임의 난수 생성

# 행렬 원소 정렬
#ck_time(0)
sort1 = 
sort2 =
sort3 = 
#ck_time(1)

#ck_time(0)
sort4 = 
sort5 =
sort6 = 
#ck_time(1)

#sort7 = np.sort(m, axis=0)[::-1, :]
#
titles= ['m','sort1','sort2','sort3','sort4','sort5', 'sort6', 'sort7']
for title in titles:
    print("[%s] = \n%s\n" %(title, eval(title)))
