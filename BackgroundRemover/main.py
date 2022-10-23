import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv2.CAP_PROP_FPS, 60)
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

listImg = os.listdir('Images')
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'Images/{imgPath}')
    imgList.append(img)

indexImg = 1

while True:
    success, img = cap.read()
    img_out = segmentor.removeBG(img, imgList[indexImg], threshold=0.7)

    imgStacked = cvzone.stackImages([img, img_out], 2, 1)
    _, imgStacked = fpsReader.update(imgStacked, color=(255, 0, 255))
    #cv2.imshow('Image', img)
    #cv2.imshow('Image Out', img_out)
    print(indexImg)
    cv2.imshow('Image Out', imgStacked)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg>0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(imgList)-1:
            indexImg += 1
    elif key == ord('q'):
        break
