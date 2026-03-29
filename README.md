

---

# 🤖 Robot Detection – Hardware-Agnostic Inference Engine

A lightweight, production-ready object detection pipeline designed for robotics systems.

Built to run seamlessly across CPU, CUDA GPUs, and future custom chipsets — without changing core logic.

> **One codebase. Multiple hardware targets. Zero vendor lock-in.**

---

## 🚀 Why This Project?

Most detection pipelines are tightly coupled to NVIDIA CUDA.
This system is intentionally hardware-agnostic so your robot can deploy anywhere.

| Platform                       | Status    |
| ------------------------------ | --------- |
| ✅ CPU (AMD / Intel)            | Supported |
| ✅ NVIDIA GPU (CUDA / TensorRT) | Supported |
| 🔜 Custom Chipset / NPU        | Phase-2   |

Whether you're running on a Jetson, desktop CPU, industrial PC, or future NPU hardware — the inference flow remains the same.

---

# 🧠 Architecture

```
Camera → Preprocess → Model → Postprocess → JSON → Robot Controller
                           │
              ┌────────────┴────────────┐
              │                         │
        Phase 1 (CUDA)            Phase 2 (ONNX Runtime)
```

---

## ⚡ Phase 1 – NVIDIA / CUDA Backend

**Target:** Jetson / NVIDIA-based robots
**Engine:** TensorRT

| Component    | Details                         |
| ------------ | ------------------------------- |
| Model Format | `best.engine`                   |
| Acceleration | CUDA + TensorRT                 |
| Performance  | Ultra-low latency GPU inference |

Used when CUDA is available.

---

## 🧩 Phase 2 – Generic / Custom Hardware Backend

**Target:** CPU / AMD / Intel / Future NPU

| Component    | Details                   |
| ------------ | ------------------------- |
| Model Format | `best.onnx`               |
| Runtime      | `onnxruntime`             |
| OS Support   | Linux / Windows           |
| Future Ready | Custom NPU SDK compatible |

Designed so you can replace `onnxruntime` with:

* OpenVINO (Intel)
* Vendor NPU SDK
* Custom accelerator runtime
* TensorRT (if needed)

No changes required to:

* Model format
* Preprocessing
* Postprocessing
* Output structure

---

# 📂 Project Structure

```
detection/
│── infer_auto.py        # Auto hardware detection (image inference)
│── infer_live.py        # Real-time camera + obstacle logic
│── models/
│   ├── phase1_cuda/
│   │   ├── best.pt
│   │   └── best.engine
│   └── phase2_generic/
│       └── best.onnx
│── logs/
│   └── run_log.jsonl    # Runtime telemetry logs
│── test.jpg
│── requirements.txt
│── README.md
```

---

# ⚙️ Setup

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

# ▶️ Run (Recommended – Auto Hardware Detection)

```bash
python infer_auto.py
```

`infer_auto.py` automatically:

* Detects CUDA availability
* Uses TensorRT engine if GPU is present
* Falls back to ONNX CPU model otherwise
* Generates both visual and structured outputs

---

# 📤 Outputs

### 🖼 output.jpg

Image with bounding boxes drawn.

### 📄 detections.json

Structured detection output for robot control logic.

Example:

```json
[
  {
    "class_id": 0,
    "confidence": 0.87,
    "bbox": [120, 45, 300, 410]
  }
]
```

This file is consumed by navigation or motion decision modules.

---

# 📊 Performance Metrics

During inference, runtime statistics are displayed.

### Example (CPU – AMD)

| Stage       | Time             |
| ----------- | ---------------- |
| Preprocess  | 20 ms            |
| Inference   | 288 ms           |
| Postprocess | 21 ms            |
| Total       | ~330 ms (~3 FPS) |

On NVIDIA GPU (Phase-1), inference latency is significantly lower.

These metrics help you:

* Benchmark hardware performance
* Choose deployment platform
* Optimize real-time robotics pipelines

---

# 🎥 Real-Time Camera Mode

Run live detection with obstacle-aware decision logic:

```bash
python infer_live.py
```

This mode:

* Auto-detects hardware backend
* Runs live webcam inference
* Applies obstacle avoidance rules
* Displays FPS + robot action
* Saves runtime logs

Press `q` to exit.

---

# 📊 Runtime Logging

Each processed frame is saved to:

```
logs/run_log.jsonl
```

Each entry includes:

* Timestamp
* FPS
* Robot action
* Detected objects
* Bounding boxes
* Object center coordinates

Example:

```json
{
  "timestamp": "2026-03-03T21:10:45.123456",
  "fps": 2.95,
  "action": "STOP - Obstacle Too Close",
  "detections": [
    {
      "label": "person",
      "confidence": 0.91,
      "bbox": [120, 45, 300, 410],
      "center": [210, 227]
    }
  ]
}
```

This enables:

* Debugging
* Performance benchmarking
* Robotics decision analysis
* Safety validation

---

# 🧩 Deployment Guide

To integrate into a robotics system, you only need:

1. `best.onnx` (Phase-2) **or** `best.engine` (Phase-1)
2. `infer_auto.py`
3. Camera feed integration

### Example Flow

```
Robot Camera → infer_auto.py → detections.json → Motion Controller → Motors
```

---

## Embedded Systems Adaptation

To integrate with specialized hardware:

Replace `onnxruntime` with:

* OpenVINO
* Vendor NPU SDK
* TensorRT
* Custom runtime

Core inference pipeline remains unchanged.

---

# 🛣️ Roadmap

| Feature                           | Status         |
| --------------------------------- | -------------- |
| CPU inference (hardware-agnostic) | ✅ Completed    |
| ONNX export                       | ✅ Completed    |
| CUDA backend                      | ✅ Completed    |
| Real-time camera stream           | 🔜 In Progress |
| Obstacle-aware decision logic     | 🔜 In Progress |
| OpenVINO backend                  | 🔜 Planned     |
| Custom chipset runtime (Phase-2)  | 🔜 Planned     |
| ROS2 integration                  | 🔜 Planned     |

---

# 🧠 Design Philosophy

> **Model should never care about the hardware.
> Hardware should adapt to the model.**

Built for real-world robots — not just demos.

---

# 🆘 Troubleshooting

### Image Not Found Error

**Problem:**

```
cv2.imread(...) returned None
```

**Fix:**

```bash
wget https://ultralytics.com/images/zidane.jpg -O test.jpg
```

---

### ONNX Output Mismatch

**Problem:** Model outputs do not match expected shape.

**Solution:** Export correctly:

```bash
yolo export model=best.pt format=onnx imgsz=640
```

---

# 👨‍💻 Maintainers

**Robotics for Human – Detection Team**

Production-focused perception systems for autonomous robotics.

---

