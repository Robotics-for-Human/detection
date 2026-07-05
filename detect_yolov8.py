from ultralytics import YOLO

model = YOLO("models/yolov8/best.pt")
model.predict(source=0, conf=0.4, show=True, save=False)
