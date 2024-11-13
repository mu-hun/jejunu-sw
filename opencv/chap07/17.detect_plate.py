import numpy as np, cv2

while True:
    

    fname = "chap07/images/test_car/{0:02d}.jpg".format(no)
    image = cv2.imread(fname, cv2.IMREAD_COLOR)
    
    
    mask = 
    gray =
    gray = 
    gray = 
    _, th_img = 
    morph = 

    cv2.imshow("image", image)
    cv2.imshow("binary image", th_img)
    cv2.imshow("opening", morph)
    cv2.waitKey()
