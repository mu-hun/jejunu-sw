import numpy as np, cv2, pickle, gzip, os
from urllib.request import urlretrieve
import matplotlib.pyplot as plt

def find_value_position(img, direct):
    project = cv2.reduce(img, direct, cv2.REDUCE_AVG).ravel()
    p0, p1 = -1, -1                                                 # 초기값
    len = project.shape[0]                                   # 전체 길이
    for i in range(len):
        if p0 < 0 and project[i] < 250: p0 = i
        if p1 < 0 and project[len-i-1] < 250 : p1 = len-i-1
    return p0, p1

# 숫자 객체 셀 중심 배치
def place_middle(number, new_size):
    h, w = number.shape[:2]
    big = max(h, w)
    square = np.full((big, big), 255, np.float32)  # 실수 자료형

    dx, dy = np.subtract(big, (w,h))//2
    square[dy:dy + h, dx:dx + w] = number
    return cv2.resize(square, new_size).flatten()  # 크기변경 및 벡터변환 후 반환


def find_number(part):
    x0, x1 = find_value_position(part, 0)  # 수직 투영
    y0, y1 = find_value_position(part, 1)  # 수평 투영
    return part[y0:y1, x0:x1]

def find_number2(part):
    contours = cv2.findContours(~part, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    rois = [cv2.boundingRect(contour) for contour in contours]
    rois = [(x, y, x+w, y+h) for x, y, w, h in rois ]   # 사각형을 시작점 종료점으로 표시

    if rois:                                # 분리된 문자 영역 누적
        pts= np.sort(rois, axis=0)             # y 방향 정렬
        x0, y0 = pts[ 0, 0:2]                  # 시작좌표 중 최소인 x, y 좌표
        x1, y1 = pts[-1, 2:]                         # 종료좌표 중 최대인 x, y 좌표
        w, h = x1-x0, y1-y0                             # 너비, 높이 계산
        part = part[y0:y0+h, x0:x0+w]
    return part

def get_cell(img, j, i, size):
    x, y = (j * size[0], i * size[1])  # 숫자칸 시작좌표
    return img[y:y + size[1], x:x + size[0]]

def load_mnist(filename):
    if not os.path.exists(filename):
        print("Downloading" )
        link = "http://deeplearning.net/data/mnist/mnist.pkl.gz"
        urlretrieve(link, filename)

    with gzip.open(filename, 'rb') as f:
        return pickle.load(f, encoding='latin1')

def graph_image(data, lable, title, nsample):
    plt.figure(num=title, figsize=(6, 9))
    rand_idx = np.random.choice(range(data.shape[0]), nsample)

    for i, id in enumerate(rand_idx):
        img = data[id].reshape((28, 28))
        plt.subplot(6, 4, i + 1), plt.axis('off'), plt.imshow(img, cmap='gray')
        plt.title(title + str(lable[id]))
    plt.tight_layout(), plt.show()