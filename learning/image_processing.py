import cv2
import os
from datetime import datetime

# Open the default webcam
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open the webcam.")
    exit()

# Create snapshots folder if it doesn't exist
os.makedirs("snapshots", exist_ok=True)

# Variable to track grayscale mode
gray_mode = False

while True:
    # Read a frame
    ret, frame = camera.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Resize the frame
    frame = cv2.resize(frame, (640, 480))

    # Print frame shape
    print(frame.shape)

    # Convert to grayscale if enabled
    if gray_mode:
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        display_frame = cv2.cvtColor(display_frame, cv2.COLOR_GRAY2BGR)
        mode_text = "Mode: Grayscale"
    else:
        display_frame = frame.copy()
        mode_text = "Mode: Color"

    # Project title
    cv2.putText(
        display_frame,
        "Edge AI Surveillance",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Current mode
    cv2.putText(
        display_frame,
        mode_text,
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    # Rectangle
    cv2.rectangle(
        display_frame,
        (100, 100),
        (300, 300),
        (255, 0, 0),
        2
    )

    # Show the camera feed
    cv2.imshow("Edge AI Surveillance - Learning OpenCV", display_frame)

    # Read keyboard input
    key = cv2.waitKey(1) & 0xFF

    # Toggle grayscale
    if key == ord('g'):
        gray_mode = not gray_mode
        print(f"Grayscale Mode: {'ON' if gray_mode else 'OFF'}")

    # Save screenshot
    elif key == ord('s'):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"snapshots/{timestamp}.jpg"

        success = cv2.imwrite(filename, display_frame)

        if success:
            print(f"✅ Screenshot saved: {filename}")
        else:
            print("❌ Failed to save screenshot.")

    # Quit
    elif key == ord('q'):
        break

# Release the camera
camera.release()

# Close all OpenCV windows
cv2.destroyAllWindows()