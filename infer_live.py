import torch
import os
import cv2
import time
from ultralytics import YOLO

# ----------------------------
# Auto Model Selection
# ----------------------------
if torch.cuda.is_available() and os.path.exists("models/phase1_cuda/best.engine"):
    print("✅ Using CUDA model")
    MODEL_PATH = "models/phase1_cuda/best.engine"
else:
    print("⚠️ Using CPU ONNX model")
    MODEL_PATH = "models/phase2_generic/best.onnx"

model = YOLO(MODEL_PATH)
CLASS_NAMES = model.names

# ----------------------------
# Robot Decision Logic
# ----------------------------
def robot_decision(detections, frame_width):
    action = "MOVE FORWARD"

    for det in detections:
        label = det["label"]
        x1, y1, x2, y2 = det["bbox"]

        box_width = x2 - x1
        box_area = box_width * (y2 - y1)

        # If object large in frame → close obstacle
        if box_area > 50000:
            action = "STOP - Obstacle Too Close"

        # If person detected in center area
        center_x = det["center"][0]
        if frame_width * 0.4 < center_x < frame_width * 0.6:
            if label == "person":
                action = "SLOW DOWN - Person Ahead"

    return action

# ----------------------------
# Start Camera
# ----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise Exception("❌ Could not open camera")

print("🎥 Live detection started... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_height, frame_width = frame.shape[:2]

    start = time.time()
    results = model(frame, conf=0.4)
    end = time.time()

    fps = 1 / (end - start)

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
                "label": label,
                "confidence": conf,
                "bbox": [x1, y1, x2, y2],
                "center": [center_x, center_y]
            })

            # Draw box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, f"{label}:{conf:.2f}", (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    # Get robot decision
    action = robot_decision(detections, frame_width)

    # Display action + FPS
    cv2.putText(frame, f"Action: {action}", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

    cv2.putText(frame, f"FPS: {round(fps,2)}", (20,80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)

    cv2.imshow("RoboDog Vision", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
