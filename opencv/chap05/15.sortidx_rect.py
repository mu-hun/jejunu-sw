import numpy as np, cv2

def print_rects(rects):
    print("-" * 46)                             	# 라인 출력
    print("사각형 원소\t\t랜덤 사각형 정보\t\t   넓이")
    print("-" * 46)
    for i, (x,y, w,h, a) in enumerate(rects):		# 저장 데이터 출력
         print("rects[%i] = [(%3d,%3d) from (%3d,%3d)] %5d" %(i, w, h, x, y, a))
    print()

rands = 
starts = 
ends = 

sizes = 
sizes0 =

areas = 
rects = 



idx = cv2.sortIdx(areas, cv2.SORT_EVERY_COLUMN).flatten()
# idx = np.argsort(areas, axis=0)

print_rects(rects)
print_rects(rects[idx.astype('int')])

## 리스트 생성 방식
# rects = ["[(%3d,%3d) from (%3d,%3d)]" %(p[0], p[1], s[0], s[1])
#          for p, s in zip(starts, sizes)]				# 시작좌표와 크기로 리스트 생성
# areas = [s[0]*s[1] for s in sizes]					# 넓이 계산 및 리스트에 저장
#
# # 정렬 후, 정렬 원소의 원본 좌표 반환
# sort_idx = cv2.sortIdx(np.array(areas), cv2.SORT_EVERY_COLUMN)
# sort_idx = map(int , sort_idx)
#
# print("-" * 46)                             	# 라인 출력
# print("사각형 원소\t\t랜덤 사각형 정보\t  크기")
# print("-" * 46)
# for i, rect, area in zip(range(5), rects, areas):		# 저장 데이터 출력
#     print("rects["+ str(i) + "] =", rect, area)
#
# print()
# print("-" * 46)
# print("사각형 원소\t\t정렬 사각형 정보\t  크기")
# print("-" * 46)
# for idx in sort_idx:									# 정렬 데이터 출력
#     print("rects[" + str(idx) + "] =", rects[idx], areas[idx])


