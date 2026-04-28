import os
import cv2
import glob

img_path = r'C:\Users\UserK\Desktop\OpenCV_data\OpenCV_Day1\ch01\images'

# 경로의 모든 파일 목록 가져오기
file_list = os.listdir(img_path)

# jpg파일만 골라 리스트 만들기 
# img_files = [os.path.join(img_path, file) 
#              for file in file_list if file.endswith('.jpg')]
# glob 라이브러리로 동일한 작업 가능(경로 다 써주거나, img_path에 저장했으므로 f-string 사용)
# img_files = glob.glob(fr"{img_path}\*.jpg")
# 또 다른 방법 
img_files = glob.glob(os.path.join(img_path, '*.jpg'))

# 전체 화면 출력 창 만들기 
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

# 불러온 이미지 반복 출력 
cnt = len(img_files)
idx = 0

while True:
    img =cv2.imread(img_files[idx])

    if img is None:
        print('image load failed!')
        break

    cv2.imshow('image',img)
    if cv2.waitKey(1000) >= 0:
        break
    
    idx += 1
    if idx >= cnt:
        idx = 0
