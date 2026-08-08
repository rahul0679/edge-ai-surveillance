import cv2

from src.detection.detector import Detector

detector = Detector()

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    if not ret:
        break

    frame, fps, threats = detector.detect(frame)

    cv2.putText(
        frame,
        f"FPS: {fps}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Threats: {threats}",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow("ThirdEye AI Cam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()