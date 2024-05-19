import base64
import math
import time

import cv2
import eel
from ultralytics import YOLO
import threading

from classes import classColors, classNames

cap = cv2.VideoCapture(0)
cap.read()
model = YOLO("../runs/best.pt", verbose=False)


#model.cuda()

def start_server():
    eel.init('static')
    eel.start('index.html', size=(800, 800))


server = threading.Thread(target=start_server).start()


@eel.expose
def start_send_camera_image():
    cameraThread = threading.Thread(target=camera_image).start()


def camera_image():
    while True:
        success, frame = cap.read()
        _, img_encoded = cv2.imencode('.jpg', frame)
        encoded_img_base64 = base64.b64encode(img_encoded.tobytes()).decode('utf-8')

        # Increment counter

        response = {'predictions_image': encoded_img_base64}

        eel.camera_image(response)()
def camera_image_model():
    while True:
        success, frame = cap.read()
        results = model(frame, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                cls = int(box.cls[0])
                class_name = classNames[cls]
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), classColors[cls], 3)
                confidence = math.ceil((box.conf[0] * 100)) / 100
                cv2.rectangle(frame, (x1 - 2, y1 - 30), (x2 + 2, y1), classColors[cls], -1)
                org = [x1, y1 - 5]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (0, 0, 0)
                thickness = 2
                cv2.putText(frame, str(class_name), org, font, fontScale, color, thickness)
                cv2.putText(frame, str(confidence), [x2 - 70, y1 - 5], font, fontScale, color, thickness)

        _, img_encoded = cv2.imencode('.jpg', frame)
        encoded_img_base64 = base64.b64encode(img_encoded.tobytes()).decode('utf-8')

        # Increment counter

        response = {'predictions_image': encoded_img_base64}

        eel.camera_image(response)()
