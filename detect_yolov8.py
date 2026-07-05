from ultralytics import YOLO
import argparse

def main():
    parser = argparse.ArgumentParser(description="Fire & Smoke Detection using YOLOv8")
    parser.add_argument("--source", required=True, help="Path to image/video or 0 for webcam")
    parser.add_argument("--conf", type=float, default=0.4, help="Confidence threshold")
    parser.add_argument("--save", action="store_true", help="Save output")
    args = parser.parse_args()

    model = YOLO("models/yolov8/best.pt")
    model.predict(source=args.source, conf=args.conf, save=args.save, show=False)

if __name__ == "__main__":
    main()
