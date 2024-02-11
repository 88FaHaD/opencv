import cv2
import numpy as np

img1=cv2.imread('A.jpg')
imsize=cv2.resize(img1,(500,500))

pts1=np.float32([[200,240],[150,180],[120,250],[140,300]])
print(pts1)
for x in range(0, 4):
    center = (int(pts1[x][0]), int(pts1[x][1]))  # Convert coordinates to integers
    cv2.circle(imsize, center, 5, (0, 255, 0), 5)

cv2.imshow('win', imsize)
cv2.waitKey(0)
cv2.destroyAllWindows()