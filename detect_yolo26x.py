from ultralytics import YOLO
import cv2

model = YOLO("models/yolo26x/best.pt")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("Starting detection... Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame, conf=0.4, verbose=False)
    annotated = results[0].plot()

    for box in results[0].boxes:
        cls = results[0].names[int(box.cls)]
        conf = float(box.conf)
        print(f"Detected: {cls} | Confidence: {conf:.2f}")

    resized = cv2.resize(annotated, (960, 540))
    cv2.imshow("Fire & Smoke Detection - YOLO26X", resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
