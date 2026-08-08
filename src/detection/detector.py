import cv2
import time
import os
from datetime import datetime

from ultralytics import YOLO

from src.utils.database import create_table, insert_detection
from src.alerts.notification import show_notification
from src.alerts.alarm import play_alarm


class Detector:

    def __init__(self):

        print("Loading YOLO Model...")
        self.model = YOLO("yolov8n.pt")
        print("YOLO Model Loaded Successfully!")

        create_table()

        self.THREAT_CLASSES = {
            "person",
            "car",
            "bus",
            "truck",
            "motorcycle"
        }

        self.CONFIDENCE_THRESHOLD = 0.70

        self.LOG_COOLDOWN = 5

        self.last_logged = {}

        self.previous_time = time.time()

        os.makedirs("snapshots", exist_ok=True)

        print("Detector Initialized Successfully!")

    def detect(self, frame):

        # Resize Frame
        frame = cv2.resize(frame, (640, 480))

        # FPS Calculation
        current_time = time.time()

        fps = (
            1 / (current_time - self.previous_time)
            if current_time > self.previous_time
            else 0
        )

        self.previous_time = current_time

        # YOLO Detection
        results = self.model(frame)

        annotated_frame = frame.copy()

        threat_count = 0
        latest_threat = None

        for box in results[0].boxes:

            class_id = int(box.cls[0])
            class_name = self.model.names[class_id]

            confidence = float(box.conf[0])

            if confidence < self.CONFIDENCE_THRESHOLD:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            is_threat = class_name in self.THREAT_CLASSES

            if is_threat:
                threat_count += 1
                latest_threat = class_name
                color = (0, 0, 255)
                label = f"THREAT: {class_name} ({confidence:.2f})"
            else:
                color = (0, 255, 0)
                label = f"{class_name} ({confidence:.2f})"

            cv2.rectangle(
                annotated_frame,
                (x1, y1),
                (x2, y2),
                color,
                2
            )

            cv2.putText(
                annotated_frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

            # Threat Logging
            if is_threat:

                now = time.time()

                if (
                    class_name not in self.last_logged
                    or
                    now - self.last_logged[class_name] >= self.LOG_COOLDOWN
                ):

                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                    snapshot_path = (
                        f"snapshots/{timestamp}_{class_name}.jpg"
                    )

                    cv2.imwrite(snapshot_path, annotated_frame)

                    insert_detection(
                        timestamp,
                        class_name,
                        confidence,
                        snapshot_path
                    )
                    # Desktop Notification
                    show_notification(
                        class_name.capitalize(),
                        confidence
                    )

                    # Alarm
                    play_alarm()

                    self.last_logged[class_name] = now

                    

        return (
            annotated_frame,
            int(fps),
            threat_count,
            latest_threat
        )