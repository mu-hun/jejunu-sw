import numpy as np, cv2

image = cv2.imread("chap05/images/bit_test.jpg", cv2.IMREAD_COLOR)  # 원본 영상 읽기
logo = cv2.imread("chap05/images/logo.jpg", cv2.IMREAD_COLOR)  # 로고 영상 읽기
if image is None or logo is None:
    raise Exception("영상 파일 읽기 오류 ")

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]  # 로고 영상 이진화
split_masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(split_masks[0], split_masks[1])
fg_pass_mask = cv2.bitwise_or(fg_pass_mask, split_masks[2])
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

(H, W), (h, w) = image.shape[:2], logo.shape[:2]  # 영상과 로고 영상의 크기
x, y = (W - w) // 2, (H - h) // 2  # 영상 가운데 위치 계산
roi = image[y : y + h, x : x + w]  # 관심 영역(roi) 지정

cv2.imshow("split_masks[0]", split_masks[0])
cv2.imshow("split_masks[1]", split_masks[1])
cv2.imshow("split_masks[2]", split_masks[2])

cv2.imshow("fg_pass_mask", fg_pass_mask)


# 행렬 논리곱과 마스킹을 이용한 관심 영역 복사
foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)
background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)

merged_image = cv2.add(foreground, background)  # 로고 합성
image[y : y + h, x : x + w] = merged_image  # 합성 영상을 원본에 복사

cv2.imshow("background", background)
cv2.imshow("forground", foreground)
cv2.imshow("dst", merged_image)
cv2.imshow("image", image)
cv2.waitKey()
