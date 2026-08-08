# ThirdEye AI Cam

ThirdEye AI Cam is an AI-powered desktop surveillance system that performs real-time object detection using YOLOv8. It identifies potential threats, stores detection history in SQLite, captures snapshots, triggers desktop notifications, and plays alarm sounds — all while running completely offline.

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
- [x] Webcam integration
- [x] Grayscale mode
- [x] FPS counter
- [x] Manual screenshot capture
- [x] YOLO object detection
- [x] Threat classification
- [x] Automatic threat screenshots
- [x] SQLite database logging
- [ ] Desktop notifications
- [ ] Alarm system
- [ ] GUI dashboard
- [ ] Detection history viewer
- [ ] Performance optimization

## 🚀 Learning Journey

This repository is being built from scratch while learning Computer Vision and Edge AI. Every feature is implemented step by step to understand how a real-world AI surveillance application works.

## 📅 Latest Update

Completed OpenCV basics:

* Live webcam feed
* Frame inspection
* Text overlay
* Rectangle drawing
