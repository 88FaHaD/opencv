import cv2 
img=cv2.imread('eagle.jpg')
#converting to gray scale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('window',gray)
cv2.waitKey(0)


#blur
blur= cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow('win',blur)
cv2.waitKey(0)


#edgecascade
can=cv2.Canny(img,125,165)
cv2.imshow('can',can)
cv2.waitKey(0)


#dillating the edge
dillat=cv2.dilate(can,(7,7),iterations=3)
cv2.imshow('dill',dillat)
cv2.waitKey(0)

#resize
resize=cv2.resize(img,(800,800))
cv2.imshow('size',resize)
cv2.waitKey(0)