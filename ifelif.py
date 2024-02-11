import cv2
img=cv2.imread('eagle.jpg',1)
cv2.imshow('window',img)

k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k == ord ('s'):
    cv2.imwrite('new eagle.png',img)
    cv2.destroyAllWindows()