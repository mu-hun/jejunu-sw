import numpy as np, cv2

x = 
y = 





print("[x] 형태: %s 원소: %s" % ( x.shape, x))
print("[mag] 형태: %s 원소: %s" % ( mag.shape, mag))

print(">>>열벡터를 1행에 출력하는 방법")
print("[m_mag] = %s" % mag.T)
print("[p_mag] = %s" % np.ravel(p_mag))
print("[p_ang] = %s" % np.ravel(p_ang))
print("[x_mat2] = %s" % x2.flatten())
print("[y_mat2] = %s" % y2.flatten())
