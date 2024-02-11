import cv2

# Load the pre-trained Haar Cascade classifier for bird detection
bird_cascade = cv2.CascadeClassifier('cascade_226.xml')

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect birds in the frame
    birds = bird_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Check if birds are detected
    if len(birds) > 0:
        print("Bird detected!")

        # Draw rectangles around the detected birds
        for (x, y, w, h) in birds:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Real-Time Bird Detection', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()

