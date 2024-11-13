import numpy as np, cv2, time

# 회선 수행 함수 - 행렬 처리 방식(속도 면에서 유리)
def filter(image, mask):
    




    return dst                                                  # 자료형 변환하여 반환

# 회선 수행 함수 - 화소 직접 근접
def filter2(image, mask):
    






    return dst

image = cv2.imread("chap07/images/filter_blur.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

# 블러링 마스크 원소 지정     
data = [



````````]
mask = np.array(data, np.float32).reshape(3, 3)
blur1 = filter(image, mask)                                    # 회선 수행 - 화소 직접 접근
blur2 = filter2(image, mask)                                   # 회선 수행

cv2.imshow("image", image)
cv2.imshow("blur1", blur1.astype("uint8"))
cv2.imshow("blur2", cv2.convertScaleAbs(blur2))
cv2.waitKey(0)