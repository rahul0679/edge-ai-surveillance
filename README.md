# ThirdEye AI Cam

## AI-Powered Real-Time Surveillance System

ThirdEye AI Cam is an offline desktop-based surveillance application that uses computer vision and YOLO object detection to identify potential threats through a live webcam feed.

The system provides real-time object detection, threat classification, snapshot capture, database logging, desktop notifications, and an audible alarm.

---

## Features

- Real-time webcam monitoring
- YOLO-based object detection
- Threat classification
- Confidence threshold filtering
- Real-time FPS monitoring
- Threat counter
- Bounding-box visualization
- Automatic threat snapshots
- SQLite detection history
- Desktop notifications
- Audible threat alarm
- Detection History dashboard
- Snapshot viewer
- Start / Stop camera controls
- Offline processing

---

## Threat Classes

The current system treats the following detected objects as threats:

- Person
- Car
- Bus
- Truck
- Motorcycle

The confidence threshold is currently set to:

```text
70% 

Technology Stack
Technology	Purpose
Python	Core programming language
OpenCV	Camera and image processing
YOLO / Ultralytics	Object detection
Tkinter	Desktop GUI
Pillow	Image handling
SQLite	Detection database
NumPy	Numerical processing
Git & GitHub	Version control
Project Structure
ThirdEye-AI-Cam/
│
├── main.py
├── requirements.txt
├── README.md
├── yolov8n.pt
│
├── snapshots/
│
├── database/
│
└── src/
    │
    ├── alerts/
    │   ├── alarm.py
    │   └── notification.py
    │
    ├── camera/
    │   └── camera.py
    │
    ├── detection/
    │   └── detector.py
    │
    ├── gui/
    │   ├── dashboard.py
    │   └── app.py
    │
    └── utils/
        └── database.py
How It Works
Webcam
   ↓
Camera Module
   ↓
Frame Capture
   ↓
YOLO Object Detection
   ↓
Confidence Filtering
   ↓
Threat Classification
   ↓
┌───────────────┬────────────────┐
│               │                │
Snapshot       SQLite          Alert
   │            Database       System
   │               │              │
   └───────────────┴──────────────┘
                   ↓
             Dashboard
Installation
1. Clone the repository
git clone https://github.com/rahul0679/edge-ai-surveillance.git
cd edge-ai-surveillance
2. Create a virtual environment

Windows:

python -m venv venv
3. Activate the environment
venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
Running the Application

Run:

python main.py

The ThirdEye AI Cam dashboard will open.

Click:

START CAMERA

to begin real-time monitoring.

Detection Workflow

When an object is detected:

YOLO identifies the object.
Confidence is checked.
Threat classes are identified.
A bounding box is drawn.
Threat count is updated.
A snapshot is saved.
Detection is stored in SQLite.
Desktop notification is generated.
Audible alarm is triggered.
Detection History

The Detection History section displays previously recorded detections including:

Detection ID
Timestamp
Object class
Confidence
Snapshot path

Double-clicking a detection allows the saved snapshot to be viewed.

Database

Detection information is stored locally using SQLite.

Each detection contains:

ID
Timestamp
Object Class
Confidence
Snapshot Path

No cloud database is required.

Privacy

ThirdEye AI Cam is designed for local/offline processing.

Camera frames are processed locally and detection information is stored locally in the project's SQLite database.

Future Improvements

Possible future enhancements include:

Custom-trained threat detection models
Multiple camera support
RTSP/IP camera support
Email alerts
Telegram alerts
User authentication
Detection analytics
Configurable threat classes
Configurable confidence threshold
GPU acceleration
ONNX optimization
Automatic report generation
Author

Rahul

BCA – Artificial Intelligence & Machine Learning

Project Status

Completed — Functional Prototype

ThirdEye AI Cam currently provides a working end-to-end desktop surveillance pipeline with real-time detection, alerting, snapshot capture, and database logging.