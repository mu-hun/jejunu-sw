import numpy as np, math, cv2
from  Common.utils import contain

# 크기 변경 함수
def scaling(img, size):                                # 크기 변경 함수
    dst = np.zeros(size[::-1], img.dtype)               # 행렬과 크기는 원소가 역순
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, img.shape[0], 1)
    j = np.arange(0, img.shape[1], 1)
    i, j = np.meshgrid(i, j)
    y, x = np.int32(i * ratioY), np.int32(j * ratioX)
    dst[y,x] = img[i,j]
    return dst

def scaling_nearest(img, size):                                # 크기 변경 함수
    dst = np.zeros(size[::-1], img.dtype)               # 행렬과 크기는 원소가 역순
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])

    i = np.arange(0, size[1], 1)
    j = np.arange(0, size[0], 1)
    i, j = np.meshgrid(i, j)
    y, x = np.int32(i / ratioY), np.int32(j / ratioX)
    dst[i,j] = img[y,x]

    return dst

def scaling_nearest2(img, size):
    (rows, cols), (w, h) = img.shape[:2], size  # 행렬은 행,열 순서
    ratioY = h/rows                                 # 세로 변경 비율
    ratioX = w/cols                                 # 가로 변경 비율
    dst = [[img[int(i / ratioY), int(j / ratioX)]
            for j in range(w)] for i in range(h)]
    return np.array(dst, img.dtype)


def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if y >= img.shape[0]-1: y = y - 1
    if x >= img.shape[1]-1: x = x - 1

    P1, P2, P3, P4 = np.float32(img[y:y+2,x:x+2].flatten())
    alpha, beta = pt[1] - y,  pt[0] - x                   # 거리 비율

    M1 = P1 + alpha * (P3 - P1)                      # 1차 보간
    M2 = P2 + alpha * (P4 - P2)
    P  = M1 + beta  * (M2 - M1)                     # 2차 보간
    return np.clip(P, 0, 255)                       # 화소값 saturation후 반환

def scaling_bilinear(img, size):                   	# 양선형 보간
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])  # 변경 크기 비율

    dst = [[ bilinear_value(img, (j/ratioX, i/ratioY))  # for문 이용한 리스트 생성
             for j in range(size[0])]
           for i in range(size[1])]
    return np.array(dst, img.dtype)

# 평행 이동
def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)            # 목적 영상 생성
    rows, cols = img.shape[:2]

    for i in range(rows):                           # 목적 영상 순회 - 역방향 사상
        for j in range(cols):
            x = j - pt[0]                           # 좌표는 x, y 순서
            y = i - pt[1]
            if contain((y, x), img.shape): dst[i, j] = img[y, x]
    return dst

def affine_transform(img, mat):
    rows, cols = img.shape[:2]
    inv_mat = cv2.invertAffineTransform(mat)  # 어파인 변환의 역행렬
    ## 리스트 생성 방식
    pts = [np.dot(inv_mat, (j, i, 1)) for i in range(rows) for j in range(cols)]
    dst = [bilinear_value(img, p) if contain(p, img.shape[::-1]) else 0 for p in pts]
    dst = np.reshape(dst, (rows, cols)).astype('uint8')
    return dst


# pt 좌표 기준으로 회전 변환함
def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)  # 목적 영상 생성
    radian = (degree / 180) * np.pi  # 회전 각도 - 라디언
    sin_value, cos_value = math.sin(radian), math.cos(radian)  # 사인, 코사인 값 미리 계산

    for i in range(img.shape[0]):  # 목적 영상 순회 - 역방향 사상
        for j in range(img.shape[1]):
            ii, jj = i - pt[1], j - pt[0]  # 중심 좌표만큼 평행 이동
            y = -jj * sin_value + ii * cos_value + pt[1]  # 회선 변환 수식
            x = jj * cos_value + ii * sin_value + pt[0]

            if contain((y, x), img.shape):  # 입력 영상의 범위 확인
                dst[i, j] = bilinear_value(img, [x, y])  # 화소값 양선형 보간
    return dst