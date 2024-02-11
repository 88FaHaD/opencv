import cv2
import numpy as np

fh=550
wh=550
cap=cv2.VideoCapture(0)
cap.set(3,fh)
cap.set(3,wh)

while True:
    suc,img=cap.read()
    imgblur=cv2.GaussianBlur(img,(5,5),1)
    imggray=cv2.cvtColor(imgblur,cv2.COLOR_BGR2GRAY)
    