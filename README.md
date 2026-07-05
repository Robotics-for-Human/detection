# Fire & Smoke Detection

Real-time fire and smoke detection using YOLO models.

## Models
| Model | mAP50 | mAP50-95 |
|-------|-------|----------|
| YOLOv8 | - | - |
| YOLO26X | 0.845 | 0.588 |

## Usage

```bash
pip install -r requirements.txt
```

**YOLOv8:**
```bash
python detect_yolov8.py --source video.mp4 --save
```

**YOLO26X:**
```bash
python detect_yolo26x.py --source video.mp4 --save
```

Use `--source 0` for webcam.
