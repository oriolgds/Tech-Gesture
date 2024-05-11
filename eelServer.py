import base64
import math

import cv2
import eel
from ultralytics import YOLO

from classes import classColors, classNames

cap = cv2.VideoCapture(0)
model = YOLO("runs/detect/Sausage1.5/weights/best.pt", verbose=False)
model.cuda()

eel.init('static')
eel.start('index.html', size=(1000, 600), block=False)




while True:
    success, frame = cap.read()
    results = model(frame, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
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
            cv2.putText(frame, str(classNames[cls]), org, font, fontScale, color, thickness)
            cv2.putText(frame, str(confidence), [x2 - 70, y1 - 5], font, fontScale, color, thickness)
    _, img_encoded = cv2.imencode('.jpg', frame)
    encoded_img_base64 = base64.b64encode(img_encoded.tobytes()).decode('utf-8')
    response = {'message': 'Image processed successfully', 'predictions_image': encoded_img_base64}
    eel.fetchImage(response)()
    cv2.imshow(frame)
