import numpy as np, cv2

# def findCorners(image, bSize):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     ret, corners = cv2.findChessboardCorners(gray, bSize) # 코너 검출
#
#     if ret:        # 부화소(subpixel) 위치를 찾아서 코너 좌표 개선
#         criteria = (cv2.TermCriteria_MAX_ITER + cv2.TermCriteria_EPS, 30, 0.1)
#         cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
#         cv2.drawChessboardCorners(image, bSize, corners, ret)           # 코너 표시
#         cv2.imshow("file", image)
#     return ret, np.array(corners, np.float32)
#
# def calibrate_correct(points, imagePoints, image):
#     size = image.shape[1::-1]                       # 행태와 크기는 역순
#     objectPoints = [np.array(points, np.float32)] * len(imagePoints)
#
#     ret = cv2.calibrateCamera(objectPoints, imagePoints, size, None, None)
#
#     newSacle, roi = cv2.getOptimalNewCameraMatrix(ret[1], ret[2], size, 1)
#     undistorted = cv2.undistort(image, ret[1], ret[2], None, newSacle)
#     x, y, w, h = roi
#     return ret, undistorted, undistorted[y:y + h, x:x + w]  # 왜곡 영역 제거

def findCorners(image, bSize):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, bSize) # 코너 검출

    if ret:        # 부화소(subpixel) 위치를 찾아서 코너 좌표 개선
        criteria = (cv2.TermCriteria_MAX_ITER + cv2.TermCriteria_EPS, 30, 0.1)
        cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    return ret, np.array(corners, np.float32), image

def show_image(file, bSize, result):
    cv2.drawChessboardCorners(result[2], bSize, result[1], result[0])  # 코너 표시
    cv2.imshow(file, result[2])

def calibrate_correct(objectPoints, imagePoints, image):
    size = image.shape[1::-1]
    ret = cv2.calibrateCamera(objectPoints, imagePoints, size, None, None)

    newSacle, roi = cv2.getOptimalNewCameraMatrix(ret[1], ret[2], size, 1)
    undistorted = cv2.undistort(image, ret[1], ret[2], None, newSacle)
    x, y, w, h = roi
    return ret, undistorted, undistorted[y:y + h, x:x + w]  # 왜곡 영역 제거
