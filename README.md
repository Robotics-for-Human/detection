# Robo-Dog Object Detection (Phase 2 – Hardware Agnostic)

This module runs object detection using a YOLOv8 model exported to ONNX.
It works on:
- CPU (AMD / Intel)
- NVIDIA GPU (with ONNX Runtime GPU)
- Future custom chipsets

## Setup

```bash
git clone https://github.com/Robotics-for-Human/detection.git
cd detection
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
