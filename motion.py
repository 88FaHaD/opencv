import cv2
import numpy as np

cap = cv2.VideoCapture('japanesepeople.mp4')
ret, video1 = cap.read()
ret, video2 = cap.read()

while cap.isOpened() and ret:
    # Check if frames are valid
    if not ret:
        break

    # Calculate absolute difference between two consecutive frames
    diff = cv2.absdiff(video1, video2)
    
    # Convert the difference to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur to the grayscale image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply threshold to create binary image
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    
    # Dilate the thresholded image to fill gaps in contours
    dilated = cv2.dilate(thresh, None, iterations=3)
    
    # Find contours in the dilated image
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    print('Number of contours:', len(contours))
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 1500:
            continue
        cv2.rectangle(video1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(video1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 3)
    # Draw contours on the original frame (video1)
    #cv2.drawContours(video1, contours, -1, (0, 255, 0), 2)
    
    # Display the result
    cv2.imshow('Motion Detection', video1)
    
    # Update frames
    video1 = video2
    ret, video2 = cap.read()
    
    # Break the loop if the 'Esc' key is pressed
    if cv2.waitKey(40) == 27:
        break

# Release the video capture object and close all windows
cv2.destroyAllWindows()
cap.release()
