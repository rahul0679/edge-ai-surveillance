import cv2

# Open the default webcam
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open the webcam.")
    exit()

# Variable to track grayscale mode
gray_mode = False

# Continuously read frames
while True:
    # Read a frame from the webcam
    ret, frame = camera.read()

    # Check if frame was captured successfully
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Print frame shape in terminal
    print(frame.shape)

    # Resize the frame
    frame = cv2.resize(frame, (640, 480))

    # Convert to grayscale if enabled
    if gray_mode:
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert back to BGR so we can draw colored text and shapes
        display_frame = cv2.cvtColor(display_frame, cv2.COLOR_GRAY2BGR)

        mode_text = "Mode: Grayscale"
    else:
        display_frame = frame.copy()
        mode_text = "Mode: Color"

    # Draw project title
    cv2.putText(
        display_frame,
        "Edge AI Surveillance",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Display current mode
    cv2.putText(
        display_frame,
        mode_text,
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    # Draw rectangle
    cv2.rectangle(
        display_frame,
        (100, 100),
        (300, 300),
        (255, 0, 0),
        2
    )

    # Show the frame
    cv2.imshow("Edge AI Surveillance - Learning OpenCV", display_frame)

    # Read keyboard input
    key = cv2.waitKey(1) & 0xFF

    # Toggle grayscale mode
    if key == ord('g'):
        gray_mode = not gray_mode
        print(f"Grayscale Mode: {'ON' if gray_mode else 'OFF'}")

    # Quit program
    elif key == ord('q'):
        break

# Release webcam
camera.release()

# Close all OpenCV windows
cv2.destroyAllWindows()