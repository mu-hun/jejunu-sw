import numpy as np, cv2, time

def print_matInfo(name, image):                 # 행렬 정보 출력 함수
    if image.dtype == 'uint8':     mat_type = "CV_8U"
    elif image.dtype == 'int8':    mat_type = "CV_8S"
    elif image.dtype == 'uint16':  mat_type = "CV_16U"
    elif image.dtype == 'int16':   mat_type = "CV_16S"
    elif image.dtype == 'float32': mat_type = "CV_32F"
    elif image.dtype == 'float64': mat_type = "CV_64F"
    nchannel = 3 if image.ndim == 3 else 1

    # depth, channel 출력
    print("%12s: depth(%s), channels(%s) -> mat_type(%sC%d)"
          % (name, image.dtype, nchannel, mat_type,  nchannel))

# 수행시간 체크 함수
stime = 0
def ck_time(mode = 0 , msg = ""):
    global stime

    if (mode ==0 ):
        stime = time.perf_counter()

    elif (mode==1):
       etime = time.perf_counter()
       elapsed = (etime - stime)
       print("수행시간 = %.5f sec" % elapsed)  # 초 단위 경과 시간

    elif (mode == 2):
        etime = time.perf_counter()
        return (etime - stime)

    elif (mode== 3 ):
        etime = time.perf_counter()
        elapsed = (etime - stime)
        print("%s = %.5f sec" %(msg, elapsed))  # 초 단위 경과 시간

def time_check(func, image, size, title):                      ## 수행시간 체크 함수
	start_time = time.perf_counter()
	ret_img = func(image, size)
	elapsed = (time.perf_counter() - start_time) * 1000
	print("%s elapsed time = %0.2f ms" % (title, elapsed))
	return ret_img


# 문자열 출력 함수 - 그림자 효과
def put_string(frame, text, pt, value=None, color=(120, 200, 90)) :
    text = str(text) + str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2) # 그림자 효과
    cv2.putText(frame, text, pt   , font, 0.7, color, 2) # 작성 문자

def print_mat(image , name = "mat"):
    print(name)
    if len(image.shape) == 1 :
        for i in range(image.shape[0]):
            print("%2.2f " %image[i] , end='')

    elif len(image.shape) == 2 :
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                print("%s " %image[i,j], end='')
            print()

    print()

def contain(p, shape):                              # 좌표(y,x)가 범위내 인지 검사
    return 0<= p[0] < shape[0] and 0<= p[1] < shape[1]

def contain_pts(p, p1, p2):
    return p1[0] <= p[0] < p2[0] and p1[1] <= p[1] < p2[1]

# 시작점 종료점 사각형을 시작점, 크기 형식으로 변환
def rect_convert(rect):
    x0, y0, x1, y1 = rect
    pt1, pt2 = (x0, y0), (x1, y1)
    size = np.subtract(pt2, pt1)            # 두좌표 차분 - 너비 높이 계산

    return (pt1[0], pt1[1], size[0], size[1])

# 시작점과 크기로 사각형 정의
def define_rect(pt, size):
    return (pt[0], pt[1], size[0], size[1])

# 시작점 종료점으로 사각형 정의
def define_rect_pt(pt1, pt2):
    size = np.subtract(pt2, pt1)            # 두좌표 차분 - 너비 높이 계산
    return (pt1[0], pt1[1], size[0], size[1])