import cv2
import eel
from ultralytics import YOLO

from classes import classColors, classNames

cap = cv2.VideoCapture(0)
model = YOLO("runs/best.pt", verbose=False)
model.cuda()