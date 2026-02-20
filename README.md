# 👁️ Learning Computer Vision

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLOv8-blueviolet?style=for-the-badge)](https://ultralytics.com/)

## 🎯 Purpose
This repository serves as a personal journey into the world of **Computer Vision**. The core philosophy is **"learning by doing"**—building small, focused projects to master complex concepts in image processing, object detection, and deep learning.

---

## 🚀 Projects Overview

| Project Name | Description | Tech Stack | Status |
| :--- | :--- | :--- | :--- |
| [🖼️ Image to Sketch](./img-to-sketch/) | Converts standard RGB images into pencil sketches using Gaussian blurring and dodging techniques. | ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) | ✅ Complete |
| [🔍 YOLO Object Detection](./object-detection-yolo/) | Real-time object detection using YOLOv8. Includes basic inference and webcam integration. | ![Ultralytics](https://img.shields.io/badge/Ultralytics-blueviolet?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![cvzone](https://img.shields.io/badge/cvzone-blue?style=flat-square) | 🚧 In Progress |

---

## 📂 Project Structure

```text
.
├── img-to-sketch/            # Image to pencil sketch converter
│   └── main.py
├── object-detection-yolo/    # YOLOv8 implementation
│   ├── running-yolo/         # Basic image inference
│   ├── weights/              # Pre-trained YOLO weights
│   └── yolo-with-cam/        # Real-time webcam detection
└── requirements.txt
```

---

## 🛠️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/learning-computer-vision.git
   cd learning-computer-vision
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📚 Key Concepts Learned
- **Image Pre-processing:** Grayscale conversion, blurring, and thresholding.
- **Deep Learning Inference:** Loading pre-trained weights and running real-time detection.
- **Path Management:** Handling file directories robustly across different environments.

---
*Happy Coding!* 🚀
