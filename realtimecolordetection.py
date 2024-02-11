import cv2
import numpy as np
framewidth=500
frameheight=500
cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
def empty(a):
    pass
cv2.namedWindow('HSV')
cv2.resizeWindow('HSV',600,400)
cv2.createTrackbar('HUE MIN','HSV',0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)
while True:
    _,img=cap.read()
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    hmin=cv2.getTrackbarPos('HUE MIN','HSV')
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    #print(hmin)
    lower=np.array([hmin,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imghsv,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)
    #cv2.imshow('img',img)
    #cv2.imshow('oee',imghsv)
    #cv2.imshow('mask',mask)
    #cv2.imshow('result',result)
    hstak=np.hstack([img,result])
    cv2.imshow('hsta',hstak)
   



    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows