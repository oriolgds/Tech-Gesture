# Tech Gesture

### Sigue estos pasos
1. Este proyecto usa Python 3.11 (Virtual venv recomendado)
2. Instala las dependencias necesarias
```
pip install ultralytics jupyter opencv-contrib-python labelme labelme2yolo streamlit cryptography eel
```
### ¿Qué hace cada archivo??
* Collect_images.py sirve para capturar imagenes
   (Se guardan en el directorio datasets/coco/images). Puedes cambiar la variable abecedario, el numero de imagenes y el tiempo de espera entre cada captura

### Convert to yolo format
```
labelme2yolo --json_dir datasets/coco/labels
```

<h3 style="color: red">Important! ⚠️</h3>
**Change** the dataset.yaml **paths**
### Create the model
```
yolo detect train data=datasets/coco/labels/YOLODataset/dataset.yaml model=yolov8s.pt epochs=2 optimize=true cache=disk
```
#### Another config
```
yolo detect train data=datasets/coco/labels/YOLODataset/dataset.yaml model=yolov8m.pt time=1.5 save_period=3 optimize=true cache=disk
```
#### Best config for GIGABYTE
```
yolo detect train data=datasets/coco/labels/YOLODataset/dataset.yaml model=yolov8m.pt time=8 optimize=true cache=disk
```
#### Larger model
```
yolo detect train data=datasets/coco/labels/YOLODataset/dataset.yaml model=yolov8l.pt time=25 optimize=true cache=disk
```
### Validate the model
```
yolo detect val model=runs\detect\train21\weights\best.pt data=datasets/coco/labels/YOLODataset/dataset.yaml
```
### Resume training
```
yolo train resume model=runs/detect/train22/weights/last.pt data=datasets/coco/labels/YOLODataset/dataset.yaml
```
### Add new images to a pretrained model
```
yolo detect train data=datasets/coco/labels/YOLODataset/dataset.yaml model=yolov8l.pt pretrained=runs/detect/Everest1.1/weights/best.pt time=10 name=Everest1.2
```