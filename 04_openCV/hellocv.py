import sys
import cv2

print('hello opencv', cv2.__version__)
img = cv2.imread(r'C:\Users\UserK\Desktop\OpenCV_data\OpenCV_Day1\cat.bmp')

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image',img)
cv2.waitKey()

cv2.destroyAllWindows()