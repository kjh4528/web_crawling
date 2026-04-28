import sys
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('camera open failed')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    inversed = ~frame

    cv2.imshow('frame',frame)
    cv2.imshow('inversed',inversed)

    if cv2.waitKey(10) == 27: #esc
        break

cap.release()
cv2.destroyAllWindows()