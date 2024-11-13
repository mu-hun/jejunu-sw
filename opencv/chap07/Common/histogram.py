# -*- coding: utf-8 -*-
import numpy as np
import cv2, time

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full( shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]             # 한 계급 너비

    for i, h in enumerate(hist):
        x = int(round(i * gap))                         # 막대 사각형 시작 x 좌표
        w = int(round(gap))
        roi = (x, 0, w, int(h))
        cv2.rectangle(hist_img, roi, 0, cv2.FILLED)
    return cv2.flip(hist_img, 0)                        # 영상 상하 뒤집기 후 반환


def make_palate(rows):
    hue = [round(i * 180 / rows) for i in range(rows)]  # hue 값 리스트 계산
    hsv = [[(h, 255, 255)] for h in hue]                # (hue, 255,255) 화소값 계산
    hsv = np.array(hsv, np.uint8)                       # numpy 행렬의 uint8형 변환
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)         # HSV 컬러 -> BGR 컬러

# 색상으로 히스토그램 그리기
def draw_histo_hue(hist, shape=(200, 256,3)):
    hsv_palate = make_palate(hist.shape[0])                      # 색상 팔레트 생성
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)    # 정규화
    gap = hist_img.shape[1] / hist.shape[0]  # 한 계급 크기

    for i, h in enumerate(hist):
        x, w = int(round(i * gap)), int(round(gap))
        if h > 0:
            color = tuple(map(int, hsv_palate[i][0]))                    # 정수형 튜플로 변환
            cv2.rectangle(hist_img, (x,0, w,int(h) ), color , cv2.FILLED) # 팔레트 색으로 그리기

    return cv2.flip(hist_img, 0)
