import numpy as np, cv2

m1 = np.full((3, 6), 10, np.uint8)
m2 = np.full((3, 6), 50, np.uint8)
m_mask = np.zeros(m1.shape, np.uint8)
m_mask[:, 3:] = 1  # 관심 영역을 지정한 후, 1 할당, 시험에 나오기 좋은 문제!!

m_add1 = cv2.add(m1, m2)
m_add2 = cv2.add(m1, m2, mask=m_mask)

m_div1 = cv2.divide(m1, m2)
m1 = m1.astype(np.float32)
m2 = np.float32(m2)
m_div2 = cv2.divide(m1, m2)

titles = ["m1", "m2", "m_mask", "m_add1", "m_add2", "m_div1", "m_div2"]
for title in titles:
    print("[%s] = \n%s \n" % (title, eval(title)))
