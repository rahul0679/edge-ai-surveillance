import cv2
import os
import time
from datetime import datetime
from ultralytics import YOLO

# ============================================
# Load YOLO Model
# ============================================
print("Loading YOLO Model...")
model = YOLO("yolov8n.pt")
print("YOLO Model Loaded Successfully!")

# ============================================
# Open Webcam
# ============================================
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

# ============================================
# Create snapshots folder
# ============================================
os.makedirs("snapshots", exist_ok=True)

# ============================================
# Variables
# ============================================
gray_mode = False
previous_time = time.time()

# ============================================
# Main Loop
# ============================================
while True:

    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # Resize frame
    frame = cv2.resize(frame, (640, 480))

    # ----------------------------------------
    # FPS Calculation
    # ----------------------------------------
    current_time = time.time()

    fps = 1 / (current_time - previous_time)

    previous_time = current_time

    # ----------------------------------------
    # Grayscale Toggle
    # ----------------------------------------
    if gray_mode:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert back to BGR
        display_frame = cv2.cvtColor(
            gray,
            cv2.COLOR_GRAY2BGR
        )

        mode_text = "Mode: Grayscale"

    else:

        display_frame = frame.copy()

        mode_text = "Mode: Color"

    # ----------------------------------------
    # Run YOLO Detection
    # ----------------------------------------
    results = model(display_frame)

    annotated_frame = results[0].plot()

    # ----------------------------------------
    # Project Title
    # ----------------------------------------
    cv2.putText(
        annotated_frame,
        "Edge AI Surveillance",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # ----------------------------------------
    # Mode Display
    # ----------------------------------------
    cv2.putText(
        annotated_frame,
        mode_text,
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    # ----------------------------------------
    # FPS Counter
    # ----------------------------------------
    cv2.putText(
        annotated_frame,
        f"FPS: {int(fps)}",
        (20, 105),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    # ----------------------------------------
    # Instructions
    # ----------------------------------------
    cv2.putText(
        annotated_frame,
        "G = Grayscale | S = Screenshot | Q = Quit",
        (20, 460),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        2
    )

    # ----------------------------------------
    # Show Output
    # ----------------------------------------
    cv2.imshow(
        "Edge AI Surveillance - YOLO",
        annotated_frame
    )

    # ----------------------------------------
    # Keyboard Controls
    # ----------------------------------------
    key = cv2.waitKey(1) & 0xFF

    # Toggle Grayscale
    if key == ord("g"):

        gray_mode = not gray_mode

        print(
            f"Grayscale Mode: {'ON' if gray_mode else 'OFF'}"
        )

    # Save Screenshot
    elif key == ord("s"):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        filename = f"snapshots/{timestamp}.jpg"

        success = cv2.imwrite(
            filename,
            annotated_frame
        )

        if success:
            print(f"Screenshot Saved: {filename}")
        else:
            print("Failed to save screenshot.")

    # Quit
    elif key == ord("q"):
        break

# ============================================
# Cleanup
# ============================================
camera.release()
cv2.destroyAllWindows()