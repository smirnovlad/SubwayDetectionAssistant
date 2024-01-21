from ultralytics import YOLO

model = YOLO('yolov8m-pose.pt')

results = model(source='img.png', save=True, conf=0.3)