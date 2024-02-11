import cv2
#resize
path='eagle.jpg'
img=cv2.imread(path)
print(img.shape)
width,height=600,600
imgResize=(cv2.resize(img,(width,height)))
print(imgResize.shape)
cv2.imshow('win',imgResize)
cv2.waitKey(0)

#crop
path1='road.jpg'
img2=cv2.imread(path1)
img2resize=cv2.resize(img2,(700,700))
print(img2resize.shape)

cv2.imshow('rd',img2resize)
cv2.waitKey(0)

imgcropped=img2resize[350:700,0:700] # will only idsplay lanes
print(imgcropped.shape)
cv2.imshow('rde',imgcropped)
cv2.waitKey(0)


