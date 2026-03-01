import cv2
import numpy as np
import onnxruntime as ort

# Load ONNX model (CPU generic)
session = ort.InferenceSession("models/best.onnx", providers=["CPUExecutionProvider"])
input_name = session.get_inputs()[0].name

# Load image
import os

img = cv2.imread("test.jpg")
if img is None:
    raise FileNotFoundError("❌ test.jpg not found in project root. Add an image named test.jpg and retry.")
# Preprocess
img_resized = cv2.resize(img, (640, 640))
img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
img_norm = img_rgb / 255.0
img_input = np.transpose(img_norm, (2, 0, 1))[None].astype(np.float32)

# Inference
outputs = session.run(None, {input_name: img_input})

# YOLOv8 ONNX output: (1, 84, 8400) OR similar
preds = outputs[0][0].T  # shape: (num_boxes, num_classes + 4)

conf_thres = 0.4

for pred in preds:
    x, y, w, h = pred[:4]
    scores = pred[4:]
    cls_id = np.argmax(scores)
    conf = scores[cls_id]

    if conf > conf_thres:
        # Convert from center-x,center-y,width,height → x1,y1,x2,y2
        x1 = int((x - w / 2) * orig_w / 640)
        y1 = int((y - h / 2) * orig_h / 640)
        x2 = int((x + w / 2) * orig_w / 640)
        y2 = int((y + h / 2) * orig_h / 640)

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"ID:{cls_id} {conf:.2f}", (x1, max(0, y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Save result
cv2.imwrite("output.jpg", img)
print("✅ Detection done. Saved as output.jpg")
