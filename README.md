
# 🤖 Robot Detection – Hardware-Agnostic Inference (CPU/GPU/Custom Chip Ready)

Lightweight, production-ready object detection pipeline built for robots.
Runs today on CPU (AMD/Intel), CUDA GPUs, and is designed to plug into custom chipsets (Phase-2) with minimal code changes.

---

## 🚀 Why This Project?

Most detection pipelines get locked to NVIDIA CUDA.
This repo is built to be hardware-agnostic so your robot can run inference on:

| Platform | Status |
|----------|--------|
| ✅ CPU (AMD / Intel) | Supported |
| ✅ NVIDIA GPU (CUDA) | Supported |
| 🔜 Custom Chipset / NPU | Phase-2 |

* ✅ CPU (AMD / Intel)
* ✅ NVIDIA GPU (CUDA)
* 🔜 Custom Chipset / NPU (Phase-2 integration)


**One codebase. Multiple hardwares. No vendor lock-in.**

---

## 🧠 Architecture (Phase-Wise)

### Phase 1 – NVIDIA / CUDA


| Component | Details |
|-----------|---------|
| **Model Format** | best.engine (TensorRT) |
| **Speed** | Ultra-fast GPU inference |
| **Target** | Jetson / NVIDIA-based robots |

### Phase 2 – Generic / Custom Chip

| Component | Details |
|-----------|---------|
| **Model Format** | ONNX model (best.onnx) |
| **Runtime** | CPU execution using onnxruntime |
| **Compatibility** | Linux / Windows / AMD / Intel |
| **Deployment** | Custom NPU hardware ready |

```
Camera → Preprocess → Model → Postprocess → JSON → Robot Controller
                        |
                  (Phase 1: CUDA / Phase 2: ONNX Runtime)
* `best.engine` (TensorRT)
* Ultra-fast GPU inference
* Used for Jetson / NVIDIA-based robots

### Phase 2 – Generic / Custom Chip

* ONNX model (`best.onnx`)
* CPU execution using `onnxruntime`
* Works on Linux / Windows / AMD / Intel
* Can be deployed on custom NPU hardware

```
Camera → Preprocess → Model → Postprocess → JSON → Robot Controller
                         |
                   (Phase 1: CUDA / Phase 2: ONNX Runtime)

```

---

## 📂 Project Structure

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

---

## ⚙️ Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Run (Recommended – Auto Hardware Detection)

```bash
python infer_auto.py
```


**infer_auto.py automatically:**

- Uses CUDA model if GPU is available
- Falls back to ONNX CPU model otherwise
- Generates both visual and structured outputs

`infer_auto.py` automatically:

* Uses CUDA model if GPU is available
* Falls back to ONNX CPU model otherwise
* Generates both visual and structured outputs


---

## 📤 Outputs

After running inference:


| Output | Type | Purpose |
|--------|------|---------|
| **output.jpg** | Image | Visualization with bounding boxes |
| **detections.json** | JSON | Structured detection data for robot control |

### Example Output (detections.json):

### 📸 output.jpg

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

This file is consumed by robot navigation / decision modules.

---

## 📊 Performance Logs

During inference, speed metrics are displayed:

### Example (CPU – AMD):


| Metric | Time |
|--------|------|
| Preprocess | 20 ms |
| Inference | 288 ms |
| Postprocess | 21 ms |
| **Total** | **~330 ms per frame (~3 FPS)** |

```
Speed:
Preprocess: 20 ms
Inference: 288 ms
Postprocess: 21 ms
Total: ~330 ms per frame (~3 FPS)
```


On NVIDIA GPU (Phase-1), inference latency is significantly lower.

**These metrics help you:**


- Benchmark hardware performance
- Decide deployment hardware
- Optimize real-time robotics pipelines

* Benchmark hardware performance
* Decide deployment hardware
* Optimize real-time robotics pipelines


---
---

## 🎥 Real-Time Camera Mode

Run live detection with obstacle decision logic:

```bash
python infer_live.py

This mode:

Uses auto hardware detection

Runs live webcam inference

Applies obstacle avoidance rules

Displays action + FPS

Saves runtime logs

Press q to exit.


---

# ✅ 3️⃣ Add Runtime Logging Section

Add this after the real-time section.

```markdown
---

## 📊 Runtime Logging

Each frame is saved to:


logs/run_log.jsonl


Each entry contains:

- Timestamp
- FPS
- Robot action
- Detected objects
- Bounding boxes
- Object center coordinates

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

This enables debugging, performance benchmarking, and robotics decision analysis.


---


# ✅ 3️⃣ Add Runtime Logging Section

Add this after the real-time section.

```markdown
---

## 📊 Runtime Logging

Each frame is saved to:


logs/run_log.jsonl


Each entry contains:

- Timestamp
- FPS
- Robot action
- Detected objects
- Bounding boxes
- Object center coordinates

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

This enables debugging, performance benchmarking, and robotics decision analysis.


---


## 🧩 Plugging into Robot (Deployment Guide)

Your robotics team only needs:


1. **best.onnx** (Phase-2) or **best.engine** (Phase-1)
2. **infer_auto.py**
3. **Camera feed integration**

### Example Deployment Flow:

* `best.onnx` (Phase-2) or `best.engine` (Phase-1)
* `infer_auto.py`
* Camera feed integration

Example deployment flow:


```
Robot Camera → infer_auto.py → detections.json → Motion Controller → Motors
```

### For Embedded Systems:

Replace `onnxruntime` backend with:


- Vendor NPU SDK
- TensorRT
- OpenVINO
- Custom runtime

**No changes required to:**

- Model format
- Preprocessing
- Postprocessing logic

---

* Vendor NPU SDK
* TensorRT
* OpenVINO
* Custom runtime

## 🛣️ Roadmap

| Feature | Status |
|---------|--------|
| CPU inference (hardware-agnostic) | ✅ Done |
| ONNX export | ✅ Done |
| CUDA backend | ✅ Done |
| Real-time camera stream | 🔜 Planned |
| Obstacle-aware decision logic | 🔜 Planned |
| OpenVINO backend (Intel) | 🔜 Planned |
| Custom chipset runtime (Phase-2) | 🔜 Planned |
| ROS2 integration | 🔜 Planned |

---

## 🧠 Design Philosophy

> **"Model should never care about the hardware. Hardware should adapt to the model."**

---

## 🆘 Troubleshooting

### Image Not Found Error

**Problem:** `cv2.imread(...) returned None`

**Fix:**

* Model format
* Preprocessing
* Postprocessing logic

---

## 🛣️ Roadmap

* ✅ CPU inference (hardware-agnostic)
* ✅ ONNX export
* ✅ CUDA backend
* 🔜 Real-time camera stream
* 🔜 Obstacle-aware decision logic
* 🔜 OpenVINO backend (Intel)
* 🔜 Custom chipset runtime (Phase-2)
* 🔜 ROS2 integration

---

## 🧠 Design Philosophy

> “Model should never care about the hardware.
> Hardware should adapt to the model.”

---

## 🆘 Troubleshooting

### Image not found error

```
cv2.imread(...) returned None
```
Fix:


```bash
wget https://ultralytics.com/images/zidane.jpg -O test.jpg
```
---

### ONNX output mismatch


### ONNX Output Mismatch


**Problem:** Model outputs don't match expectations

**Solution:** Ensure model was exported using:

```bash

```

yolo export model=best.pt format=onnx imgsz=640
```

---

## 👨‍💻 Maintainers

**Robotics for Human – Detection Team**

Built for real-world robots, not just demos.

Built for real-world robots, not just demos.


---
