import cv2
import numpy as np

# img1 = np.empty((480,640),dtype=np.uint8)
# img2 = np.zeros((480,640,3),dtype=np.uint8)
# img3 = np.ones((480,640),dtype=np.uint8)*255
# img4 = np.full((480,640,3),(255,255,0),dtype=np.uint8)

# cv2.imshow('img1',img1)
# cv2.imshow('img2',img2)
# cv2.imshow('img3',img3)
# cv2.imshow('img4',img4)
# cv2.waitKey()

# 복사 예제 
# img1 = cv2.imread(r'C:\Users\UserK\Desktop\OpenCV_data\OpenCV_Day1\ch01\HappyFish.jpg')
# img2 = img1
# img3 = img1.copy()

# img1.fill(255)
# cv2.imshow('img1',img1)
# cv2.imshow('img2',img2)
# cv2.imshow('img3',img3)
# cv2.waitKey()

# 부분 추출
img1 = cv2.imread(r'C:\Users\UserK\Desktop\OpenCV_data\OpenCV_Day1\ch01\HappyFish.jpg')
img2 = img1[40:120,30:150]
img3 = img1[40:120,30:150].copy()
img2.fill(0)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey()