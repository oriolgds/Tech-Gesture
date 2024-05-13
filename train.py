from ultralytics import YOLO

model = YOLO('yolov8l.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='datasets\coco\labels\YOLODataset\dataset.yaml', time=500, optimize=True, name="Everest1", device=0)