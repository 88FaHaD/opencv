import cv2

img=cv2.imread('eagle.jpg',1) #read image takes two prameters image and 0,1,-1 means load img in greyscale,color or alphachannel
print(img)

cv2.imshow('window',img) #display image takes two parameters a wondow where image is to be dispalyed and the image
cv2.waitKey(1000)  #delay for 1000 seconds
cv2.destroyAllWindows()  #used to destroy the window

cv2.imwrite('eagle.png',img) # takes two 

