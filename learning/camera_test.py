import cv2


camera = cv2.VideoCapture(0)


if not camera.isOpened():
    print("Error: Could not open the webcam.")
    exit()


while True:
  
    ret, frame = camera.read()

    
    if not ret:
        print("Error: Failed to capture frame.")
        break

    
    cv2.imshow("Live Camera Feed", frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()


cv2.destroyAllWindows()