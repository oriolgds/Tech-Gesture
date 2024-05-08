import base64
import json
import math

import cv2
import numpy as np
from flask import Flask, request, jsonify
from ultralytics import YOLO
from server.classes import classColors, classNames

model = YOLO("C:\Github\Mini-Empresa/runs\detect\Sausage1.2\weights/best.pt", verbose=False)
model.cuda()

app = Flask(__name__,
            static_folder='C:\Github\Mini-Empresa\server\static',
            static_url_path='/static/',
            )


@app.route('/predict', methods=['POST'])
def predict():
    data = json.loads(request.data.decode('utf-8'))
    image_data = data.get('image')
    image_bytes = base64.b64decode(image_data.split(',')[1])
    nparr = np.frombuffer(image_bytes, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    results = model(img_np)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(img_np, (x1, y1), (x2, y2), classColors[cls], 3)
            confidence = math.ceil((box.conf[0] * 100)) / 100
            cv2.rectangle(img_np, (x1 - 2, y1 - 30), (x2 + 2, y1), classColors[cls], -1)
            org = [x1, y1 - 5]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (0, 0, 0)
            thickness = 2
            cv2.putText(img_np, str(classNames[cls]), org, font, fontScale, color, thickness)
            cv2.putText(img_np, str(confidence), [x2 - 70, y1 - 5], font, fontScale, color, thickness)
    _, img_encoded = cv2.imencode('.jpg', img_np)
    encoded_img_base64 = base64.b64encode(img_encoded.tobytes()).decode('utf-8')
    response = {'message': 'Image processed successfully', 'predictions_image': encoded_img_base64}
    return jsonify(response)





if __name__ == "__main__":
    app.run(ssl_context=('server.crt', 'server.key'), host='localhost', port=4443, debug=True)
