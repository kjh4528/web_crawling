
import cv2
import numpy as np

src = cv2.imread(r'C:\Users\UserK\Desktop\OpenCV_data\OpenCV_Day1\ch02\airplane.bmp')
mask = cv2.imread(r'C:\Users\UserK\Desktop\OpenCV_data\OpenCV_Day1\ch02\mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread(r'C:\Users\UserK\Desktop\OpenCV_data\OpenCV_Day1\ch02\field.bmp', cv2.IMREAD_COLOR)
# cv2.imshow('image1',src)
# cv2.imshow('image2',mask)
# cv2.imshow('image3',dst)
# cv2.waitKey()

cv2.copyTo(src, mask, dst)

cv2.imshow('result',dst)
cv2.waitKey()
cv2.destroyAllWindows()