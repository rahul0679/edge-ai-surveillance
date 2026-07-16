# Edge AI Surveillance

An offline desktop-based surveillance system that performs real-time object detection using Computer Vision and Edge AI without relying on cloud services.

## 📌 Project Goal

The goal of this project is to build a real-time surveillance application that can:

* Read live video from a webcam or RTSP camera
* Detect threats using AI models (YOLO)
* Display detections with bounding boxes
* Trigger desktop notifications and alarm sounds
* Save screenshots of detected threats
* Store detection logs in a local SQLite database
* Work completely offline with low latency

## 🛠️ Tech Stack

* Python
* OpenCV
* NumPy
* YOLO (Ultralytics)
* ONNX Runtime (later)
* SQLite
* CustomTkinter / PyQt (later)
* Git & GitHub

## 📂 Current Project Structure

```text
Edge-AI-Surveillance/
│
├── camera_test.py
├── frame_info.py
├── image_processing.py
├── README.md
├── requirements.txt
└── .gitignore
```

> The project structure will be improved gradually as new modules are added.

## ✅ Progress

- [x] Project setup
- [x] GitHub repository created
- [x] Git initialized
- [x] OpenCV installed
- [x] Webcam integration
- [x] Frame information (`frame.shape`)
- [x] Drawing text on video
- [x] Drawing rectangles on video
- [x] Image resizing
- [x] Grayscale mode toggle
- [x] Screenshot capture
- [x] FPS counter
- [x] YOLOv8 model integration
- [x] Real-time object detection
- [x] Custom bounding box rendering
- [x] Object labels with confidence score

### 🚧 Upcoming Features

- [ ] Threat filtering
- [ ] SQLite logging
- [ ] Desktop notifications
- [ ] Alarm sound
- [ ] GUI Dashboard
- [ ] ONNX Optimization

## 🚀 Learning Journey

This repository is being built from scratch while learning Computer Vision and Edge AI. Every feature is implemented step by step to understand how a real-world AI surveillance application works.

## 📅 Latest Update

Completed OpenCV basics:

* Live webcam feed
* Frame inspection
* Text overlay
* Rectangle drawing
