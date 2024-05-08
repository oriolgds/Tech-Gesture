import base64
import json
import math
from ultralytics import YOLO
import cv2
import numpy as np
from flask import Flask, url_for, redirect, jsonify, request

from classes import classNames, classColors

app = Flask(__name__)

model = YOLO("../runs/detect/Sausage1.2/weights/best.pt", verbose=False)
model.cuda()


@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the URL from the request
        data_url = request.json['image']
        # Split the data URL to extract the base64-encoded image data
        header, encoded = data_url.split(",", 1)

        # Decode the base64-encoded image data
        decoded = base64.b64decode(encoded)

        # Convert the decoded data to a NumPy array
        nparr = np.frombuffer(decoded, np.uint8)

        # Decode the NumPy array as an image using OpenCV
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


with app.test_request_context():
    print(url_for('static', filename='index.html'))

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
