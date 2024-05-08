from ultralytics import YOLO
import cv2


cap = cv2.VideoCapture(0)
model = YOLO("yolov8s.pt", verbose=False)

while True:
    success, frame = cap.read()
