import torch
import os
import cv2
import json
import time
from ultralytics import YOLO

IMAGE_PATH = "test.jpg"

# ----------------------------
# Model Selection (Auto Mode)
# ----------------------------
if torch.cuda.is_available() and os.path.exists("models/phase1_cuda/best.engine"):
    print("✅ Using CUDA TensorRT model")
    MODEL_PATH = "models/phase1_cuda/best.engine"
elif os.path.exists("models/phase2_generic/best.onnx"):
    print("⚠️ Using CPU/Generic ONNX model")
    MODEL_PATH = "models/phase2_generic/best.onnx"
else:
    raise FileNotFoundError(
        "❌ No model found. Put best.engine or best.onnx in models/ folder."
    )

# ----------------------------
# Load Model
# ----------------------------
model = YOLO(MODEL_PATH)

# ----------------------------
# Load Image
# ----------------------------
img = cv2.imread(IMAGE_PATH)
if img is None:
    raise FileNotFoundError("❌ test.jpg not found in repo folder")

# ----------------------------
# Inference + Speed Logging
# ----------------------------
start_time = time.time()
results = model(IMAGE_PATH, conf=0.4)
end_time = time.time()

total_time = end_time - start_time
fps = 1 / total_time

print(f"⏱ Total Inference Time: {round(total_time * 1000, 2)} ms")
print(f"🚀 FPS: {round(fps, 2)}")

# ----------------------------
# Postprocessing
# ----------------------------
CLASS_NAMES = model.names
detections = []

for r in results:
    for box in r.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])

        label = CLASS_NAMES[cls]
        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)

        detections.append({
            "class_id": cls,
            "label": label,
            "confidence": round(conf, 3),
            "bbox": [x1, y1, x2, y2],
            "center": [center_x, center_y]
        })

        # Draw bounding box
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            img,
            f"{label}:{conf:.2f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

# ----------------------------
# Save Outputs
# ----------------------------
cv2.imwrite("output.jpg", img)

with open("detections.json", "w") as f:
    json.dump(detections, f, indent=2)

print("✅ Detection complete")
print("📸 output.jpg saved")
print("📄 detections.json saved")
