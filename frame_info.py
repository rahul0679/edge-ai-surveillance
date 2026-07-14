import cv2

# Open the default webcam (0 = first camera)
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open the webcam.")
    exit()

# Continuously read frames
while True:
    # Read a frame from the webcam
    ret, frame = camera.read()

    print(frame.shape)  # Print the shape of the captured frame

    # If no frame is captured, stop the loop
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Draw text on the frame
    cv2.putText(
        frame,
        "Edge AI Surveillance",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
    
    cv2.rectangle(
        frame,
        (100, 100),
        (300, 300),
        (255, 0, 0),
        2
    )
    # Display the frame in a window
    cv2.imshow("Live Camera Feed", frame)

    # Exit when the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
camera.release()

# Close all OpenCV windows
cv2.destroyAllWindows()