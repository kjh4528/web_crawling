import matplotlib.pyplot as plt
import cv2

# 컬러 출력(cv는 기본  BGR, mat은 RGB)
imgBGR = cv2.imread(r'C:\Users\UserK\Desktop\OpenCV_data\OpenCV_Day1\cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이 스케일 출력
imgGray = cv2.imread(r'C:\Users\UserK\Desktop\OpenCV_data\OpenCV_Day1\cat.bmp',cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()


plt.subplot(121),plt.axis('off'),plt.imshow(imgRGB)
plt.subplot(122),plt.axis('off'),plt.imshow(imgGray,cmap='gray')
plt.show()