import numpy as np
import cv2

orange, blue, cyan = 
white, black =          
image = np.full((300, 500, 3), white, np.uint8)             # 

center = ( ,      )         		# 
pt1, pt2 = (300, 50), (100, 220)
shade = ()                          # 그림자 좌표

cv2.circle(               )                         #  
cv2.circle(               )
cv2.circle(               )                   #  

font = cv2.
cv2.putText(                     )
cv2.putText(                      )
cv2.putText(                           )   #  
cv2.putText(                  ))

title = "Draw circles"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.waitKey(0)