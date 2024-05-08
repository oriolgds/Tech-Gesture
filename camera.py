import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 for the default camera, change it if you have multiple cameras

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open camera")
    exit()

# Loop to capture frames from the camera
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame is empty
    if not ret:
        print("Error: Couldn't capture frame")
        break

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Check for key press; if 'q' is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
