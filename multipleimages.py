import cv2
import numpy as np

img1=cv2.imread('eagle.jpg')
print(
img1.shape)
img2=cv2.imread('road.jpg')
print(img2.shape)
img1rsize=cv2.resize(img1,(500,500))
img2rsize=cv2.resize(img2,(500,500))

#joining the image horizontally and vertically
hor=np.hstack((img1rsize,img2rsize))
ver=np.vstack((img1rsize,img2rsize))
cv2.imshow('hort',hor)
cv2.imshow('vert',ver)
cv2.waitKey(0)

