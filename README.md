🤖 Robot Detection – Hardware-Agnostic Inference (CPU/GPU/Custom Chip Ready)

Lightweight, production-ready object detection pipeline built for robots.
Runs today on CPU (AMD/Intel), CUDA GPUs, and is designed to plug into custom chipsets (Phase-2) with minimal code changes.

🚀 Why This Project?

Most detection pipelines get locked to NVIDIA CUDA.
This repo is built to be hardware-agnostic so your robot can run inference on:

✅ CPU (AMD / Intel)

✅ NVIDIA GPU (CUDA)

🔜 Custom Chipset / NPU (Phase-2 integration)

One codebase. Multiple hardwares. No vendor lock-in.

🧠 Architecture (Phase-Wise)
Phase 1 – NVIDIA / CUDA

best.engine (TensorRT)

Ultra-fast GPU inference

Used for Jetson / NVIDIA-based robots

Phase 2 – Generic / Custom Chip

ONNX model (best.onnx)

CPU execution using onnxruntime

Works on Linux / Windows / AMD / Intel

Can be deployed on custom NPU hardware

Camera → Preprocess → Model → Postprocess → JSON → Robot Controller
                         |
                   (Phase 1: CUDA / Phase 2: ONNX Runtime)
📂 Project Structure
detection/
│── infer_auto.py       # Auto hardware detection (recommended)
│── infer_cpu.py        # CPU-only inference
│── models/
│   ├── phase1_cuda/
│   │   ├── best.pt
│   │   └── best.engine
│   └── phase2_generic/
│       └── best.onnx
│── test.jpg
│── output.jpg          # Generated result
│── detections.json     # Robot-readable output
│── requirements.txt
│── README.md
⚙️ Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
▶️ Run (Recommended – Auto Hardware Detection)
python infer_auto.py

infer_auto.py automatically:

Uses CUDA model if GPU is available

Falls back to ONNX CPU model otherwise

Generates both visual and structured outputs

📤 Outputs

After running inference:

📸 output.jpg

Image with bounding boxes drawn.

📄 detections.json

Structured detection output for robot control logic.

Example:

[
  {
    "class_id": 0,
    "confidence": 0.87,
    "bbox": [120, 45, 300, 410]
  }
]

This file is consumed by robot navigation / decision modules.

📊 Performance Logs

During inference, speed metrics are displayed:

Example (CPU – AMD):

Speed:
Preprocess: 20 ms
Inference: 288 ms
Postprocess: 21 ms
Total: ~330 ms per frame (~3 FPS)

On NVIDIA GPU (Phase-1), inference latency is significantly lower.

These logs help:

Benchmark hardware performance

Decide deployment hardware

Optimize real-time robotics pipelines

🧩 Plugging into Robot (Deployment Guide)

Your robotics team only needs:

best.onnx (Phase-2) or best.engine (Phase-1)

infer_auto.py

Camera feed integration

Example deployment flow:

Robot Camera → infer_auto.py → detections.json → Motion Controller → Motors

For embedded systems:

Replace onnxruntime backend with:

Vendor NPU SDK

TensorRT

OpenVINO

Custom runtime

No changes required to:

Model format

Preprocessing

Postprocessing logic

🛣️ Roadmap

✅ CPU inference (hardware-agnostic)

✅ ONNX export

✅ CUDA backend

🔜 Real-time camera stream

🔜 Obstacle-aware decision logic

🔜 OpenVINO backend (Intel)

🔜 Custom chipset runtime (Phase-2)

🔜 ROS2 integration

🧠 Design Philosophy

“Model should never care about the hardware.
Hardware should adapt to the model.”

🆘 Troubleshooting
Image not found error
cv2.imread(...) returned None

Fix:

wget https://ultralytics.com/images/zidane.jpg -O test.jpg
ONNX output mismatch

Ensure model was exported using:

yolo export model=best.pt format=onnx imgsz=640
👨‍💻 Maintainers

Robotics for Human – Detection Team
Built for real-world robots, not just demos.
