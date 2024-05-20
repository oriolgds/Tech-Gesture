import time
from classes import classNames, classColors
from ultralytics import YOLO
import cv2
import math

# Initialize MediaPipe Hands
#mp_hands = mp.solutions.hands
#hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
# Initialize Drawing module
#mp_drawing = mp.solutions.drawing_utils

# start webcam
cap = cv2.VideoCapture(0)

# model
model = YOLO("runs/detect/Everest2.1/weights/best.pt", verbose=False)
#model.cuda()

# object classes


logo = cv2.imread('assets/Logotipo.png', cv2.IMREAD_UNCHANGED)  # Load the logo with its alpha channel if present

# Scale down the logo and get its size
scale = 0.2  # Adjust the scale as needed
logo_height, logo_width = int(logo.shape[0] * scale), int(logo.shape[1] * scale)
resized_logo = cv2.resize(logo, (logo_width, logo_height))

# Extract BGR and alpha channel if logo has an alpha channel
if resized_logo.shape[2] == 4:
    b, g, r, a = cv2.split(resized_logo)
    overlay_color = cv2.merge((b, g, r))
    mask = a
    mask_inv = cv2.bitwise_not(mask)

# In order to calc FPS
prev_time = 0

while True:
    success, frame = cap.read()
    results = model(frame, stream=True)

    # Show the logo
    frame_height, frame_width = frame.shape[:2]
    x_offset = frame_width - logo_width - 10  # Padding of 10 pixels from the right edge
    y_offset = frame_height - logo_height - 10  # Padding of 10 pixels from the bottom edge

    # Region of interest (ROI) from the frame where the logo will be placed
    roi = frame[y_offset:y_offset + logo_height, x_offset:x_offset + logo_width]

    if resized_logo.shape[2] == 4:
        # Apply the mask and combine using bitwise operations
        roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
        roi_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)

        # Combine the background and foreground in ROI
        dst = cv2.add(roi_bg, roi_fg)
        frame[y_offset:y_offset + logo_height, x_offset:x_offset + logo_width] = dst

    # Draw the landmarks from mediapipe
    # success, image_rgb = cap.read()
    # resultsMP = hands.process(image_rgb)
    # if resultsMP.multi_hand_landmarks:
    #     for hand_landmarks in resultsMP.multi_hand_landmarks:
    #         # Draw hand landmarks and connections on the image
    #         mp_drawing.draw_landmarks(image_rgb, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # coordinates
    for r in results:
        boxes = r.boxes  # Boxes object for bbox outputs

        for box in boxes:
            # class name
            cls = int(box.cls[0])
            # print("Class name -->", classNames[cls])

            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

            # put box in cam
            cv2.rectangle(frame, (x1, y1), (x2, y2), classColors[cls], 3)

            # confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)

            # Background rectangle class name
            cv2.rectangle(frame, (x1 - 2, y1 - 30), (x2 + 2, y1), classColors[cls], -1)

            # Class name
            org = [x1, y1 - 5]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (0, 0, 0)
            thickness = 2

            cv2.putText(frame, str(classNames[cls]), org, font, fontScale, color, thickness)

            # Confidence text
            cv2.putText(frame, str(confidence), [x2 - 70, y1 - 5], font, fontScale, color, thickness)

    # Calculate the time difference
    current_time = time.time()
    if prev_time != 0:
        time_diff = current_time - prev_time
        fps = 1 / time_diff
        # Display the FPS on the frame
        cv2.putText(frame, f'FPS: {fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0), 1, cv2.LINE_AA)

    prev_time = current_time
    cv2.imshow('Tech Gesture', frame)
    # cv2.imshow('Tech Gesture 2', image_rgb)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
