import torch
import os
import cv2
import json
from ultralytics import YOLO

IMAGE_PATH = "test.jpg"

if torch.cuda.is_available() and os.path.exists("models/phase1_cuda/best.engine"):
    print("✅ Using CUDA TensorRT model")
    MODEL_PATH = "models/phase1_cuda/best.engine"
    device = "cuda"
elif os.path.exists("models/phase2_generic/best.onnx"):
    print("⚠️ Using CPU/Generic ONNX model")
    MODEL_PATH = "models/phase2_generic/best.onnx"
    device = "cpu"
else:
    raise FileNotFoundError("❌ No model found. Put best.engine or best.onnx in models/ folders.")

model = YOLO(MODEL_PATH)

results = model(IMAGE_PATH, conf=0.4)

img = cv2.imread(IMAGE_PATH)
if img is None:
    raise FileNotFoundError("❌ test.jpg not found in repo folder")

detections = []

for r in results:
    for box in r.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])

        detections.append({
            "class_id": cls,
            "confidence": round(conf, 3),
            "bbox": [x1, y1, x2, y2]
        })

        cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(img, f"{cls}:{conf:.2f}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

cv2.imwrite("output.jpg", img)

with open("detections.json", "w") as f:
    json.dump(detections, f, indent=2)

print("✅ Detection complete")
print("📸 output.jpg saved")
print("📄 detections.json saved")
