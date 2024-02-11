import cv2

video=cv2.VideoCapture(0) # 0,1,-1 for cameras   and for files give file name
out=cv2.VideoWriter('file.mp4',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))

while(True):
    ret,frame=video.read()
    if ret == True:
        out.write(frame)
            
        cv2.imshow('window',frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
         break
    else:
       break    

video.release()
out.release()
cv2.destroyAllWindows() 
