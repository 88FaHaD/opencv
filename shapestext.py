import cv2
import numpy as np
#black img
img=np.zeros((512,512,3))
print(img.shape)
cv2.imshow('win',img)
cv2.waitKey(0)
#coloring the img
img[:]=(255,0,0)
cv2.imshow('wind',img)
cv2.waitKey(0)

#line
cv2.line(img,(0,0),(100,100),(0,255,0),6)
cv2.imshow('wind',img)
cv2.waitKey(0)
#rectangle
cv2.rectangle(img,(150,150),(200,200),(0,0,255),5)
cv2.imshow('wind',img)
cv2.waitKey(0)

#filling the color

cv2.rectangle(img,(150,150),(200,200),(0,0,255),cv2.FILLED)
cv2.imshow('wind',img)
cv2.waitKey(0)

#circle
cv2.circle(img,(350,335),39,(240,230,220),5)
cv2.imshow('wind',img)
cv2.waitKey(0)

#text
img3=cv2.putText(img,'shapes drawing',(200,200),cv2.FONT_HERSHEY_SIMPLEX,1,(150,85,130),3)
cv2.imshow('wind',img3)
cv2.waitKey(0)