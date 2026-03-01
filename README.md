
---

# 🤖 Robot Detection – Hardware-Agnostic Inference (CPU/GPU/Custom Chip Ready)

> Lightweight, production-ready object detection pipeline built for robots.
> Runs today on CPU (AMD/Intel), CUDA GPUs, and is designed to plug into **custom chipsets (Phase-2)** with minimal code changes.

---

## 🚀 Why This Project?

Most detection pipelines get locked to **NVIDIA CUDA**.
This repo is built to be **hardware-agnostic** so your robot can run inference on:

* ✅ CPU (AMD / Intel)
* ✅ NVIDIA GPU (CUDA)
* 🔜 Custom Chipset / NPU (Phase-2 integration)

**One codebase. Multiple hardwares. No vendor lock-in.**

---

## 🧠 Architecture (Phase-Wise)

### Phase 1 – Generic Inference (Current)

* ONNX model (`best.onnx`)
* CPU execution using `onnxruntime`
* Works on any host machine (Linux, Windows)

### Phase 2 – Custom Chipset (Planned)

* ONNX → Vendor SDK / NPU runtime
* Replace backend only (no model rewrite)
* Same preprocessing + postprocessing

```text
Camera → Preprocess → ONNX Runtime → Postprocess → Robot Controller
                         |
                   (Phase 2: Custom NPU Runtime)
```

---

## 📂 Project Structure

```text
detection/
│── infer_cpu.py        # CPU inference script (generic backend)
│── models/
│   ├── best.onnx       # Hardware-agnostic model
│   └── best.pt         # Training checkpoint
│── test.jpg            # Sample input
│── output.jpg          # Output with bounding boxes
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup (CPU – Works on AMD/Intel)

```bash
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## ▶️ Run Inference

```bash
python infer_cpu.py
```

Output:

```text
✅ Detection done. Saved as output.jpg
```

Open result:

```bash
xdg-open output.jpg
```

---

## 📦 Dependencies

```txt
onnxruntime
opencv-python
numpy
ultralytics
```

---

## 🧩 Plugging into Robot (Deployment Guide)

Your robot firmware team only needs:

* `best.onnx`
* `infer_cpu.py` (or its backend wrapper)
* Camera feed integration

Example pipeline:

```text
Robot Camera → Frame Buffer → infer_cpu.py → Detection Boxes → Motion Controller
```

For embedded systems:

* Replace `onnxruntime` with:

  * Vendor NPU SDK
  * TensorRT
  * OpenVINO
  * Custom runtime (Phase-2)

No changes to:

* Model format
* Preprocessing
* Postprocessing logic

---

## 🛣️ Roadmap

* [x] CPU inference (hardware-agnostic)
* [x] ONNX export
* [ ] CUDA backend
* [ ] OpenVINO backend (Intel)
* [ ] Custom chipset runtime (Phase-2)
* [ ] Real-time camera stream
* [ ] ROS2 integration

---

## 🧑‍💻 Maintainers

**Robotics for Human – Detection Team**
Built for real-world robots, not just demos.

---

## 🧠 Design Philosophy

> “Model should never care about the hardware.
> Hardware should adapt to the model.”

---

## 🆘 Troubleshooting

**Image not found error**

```text
cv2.imread(...) returned None
```

Fix:

```bash
wget https://ultralytics.com/images/zidane.jpg -O test.jpg
```

**ONNX output shape mismatch**

> Make sure you're using the correct YOLOv8 ONNX export.

---


