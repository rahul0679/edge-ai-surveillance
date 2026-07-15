import cv2
import os
import time
from datetime import datetime


# Open Webcam

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()


# Create snapshots folder if it doesn't exist

os.makedirs("snapshots", exist_ok=True)


# Variables

gray_mode = False

# Used for FPS calculation
previous_time = time.time()


# Main Loop

while True:

    # Read frame
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # Resize frame
    frame = cv2.resize(frame, (640, 480))

    # Print frame shape (Learning Purpose)
    print(frame.shape)

    
    # FPS Calculation
    
    current_time = time.time()

    time_difference = current_time - previous_time

    if time_difference > 0:
        fps = 1 / time_difference
    else:
        fps = 0

    previous_time = current_time

    
    # Grayscale Toggle
    
    if gray_mode:
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert back to BGR so colored drawings work
        display_frame = cv2.cvtColor(
            display_frame,
            cv2.COLOR_GRAY2BGR
        )

        mode_text = "Mode: Grayscale"

    else:
        display_frame = frame.copy()
        mode_text = "Mode: Color"

    
    # Project Title
    
    cv2.putText(
        display_frame,
        "Edge AI Surveillance",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

   
    # Current Mode
    
    cv2.putText(
        display_frame,
        mode_text,
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

   
    # FPS Display
    
    cv2.putText(
        display_frame,
        f"FPS: {fps:.2f}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    
    # Demo Rectangle
   
    cv2.rectangle(
        display_frame,
        (100, 150),
        (300, 350),
        (255, 0, 0),
        2
    )

   
    # Show Frame
    
    cv2.imshow(
        "Edge AI Surveillance - Learning OpenCV",
        display_frame
    )

   
    # Keyboard Controls
   
    key = cv2.waitKey(1) & 0xFF

    # Toggle Grayscale
    if key == ord('g'):
        gray_mode = not gray_mode
        print(f"Grayscale Mode: {'ON' if gray_mode else 'OFF'}")

    # Save Screenshot
    elif key == ord('s'):

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        filename = f"snapshots/{timestamp}.jpg"

        success = cv2.imwrite(filename, display_frame)

        if success:
            print(f"Screenshot Saved: {filename}")
        else:
            print("Failed to save screenshot.")

    # Quit
    elif key == ord('q'):
        break


# Cleanup

camera.release()
cv2.destroyAllWindows()