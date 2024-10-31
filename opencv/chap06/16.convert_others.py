import cv2

BGR_img = cv2.imread("Source/chap06/images/color_space.jpg", cv2.IMREAD_COLOR) # 컬러 영상 읽기
if BGR_img is None: raise Exception("영상 파일 읽기 오류")
    







cv2.imshow("BGR_img", BGR_img)
cv2.imshow("Gray_img", Gray_img)

sp1, sp2, sp3 = ['Y', 'Cr', 'Cb'] , ['Y', 'U', 'V'], ['L', 'A', 'B']
for i in range(len(sp1)):
    cv2.imshow("YCC_img[%d]-%s" %(i, sp1[i]), YCC_ch[i])
    cv2.imshow("YUV_img[%d]-%s" %(i, sp2[i]), YUV_ch[i])
    cv2.imshow("LAB_img[%d]-%s" %(i, sp3[i]), Lab_ch[i])
cv2.waitKey(0)