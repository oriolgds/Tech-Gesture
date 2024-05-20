import base64
import math
import threading
import time

import cv2
import eel
from ultralytics import YOLO

from classes import classColors, classNames

cap = cv2.VideoCapture(0)
model = YOLO("runs/detect/Everest2.1/weights/best.pt", verbose=False)

last_detection_time = {}  # Un diccionario para rastrear el tiempo de la última detección de cada clase


def start_server():
    @eel.expose
    def start_process():
        process()
    eel.init('static')
    eel.start('index.html', size=(1000, 600))


# Initialize counter variable




def process():
    counter = 0

    # Start time
    start_time = time.time()
    while True:
        success, frame = cap.read()
        results = model(frame, stream=True)
        detectedClasses = []
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

                # Añadir la classe al array de detecciones
                if detectedClasses.count(class_name) == 0:
                    detectedClasses.append(class_name)

        _, img_encoded = cv2.imencode('.jpg', frame)
        encoded_img_base64 = base64.b64encode(img_encoded.tobytes()).decode('utf-8')

        # Increment counter
        counter += 1

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        response = {'message': 'Image processed successfully', 'predictions_image': encoded_img_base64,
                    'detectedClasses': detectedClasses, 'elapsedTime': elapsed_time}

        eel.fetchImage(response)()


serverThread = threading.Thread(target=start_server)
serverThread.start()

