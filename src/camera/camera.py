import cv2


class Camera:

    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self.cap = None

    def start(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(
                self.camera_id,
                cv2.CAP_DSHOW
            )

        return self.cap.isOpened()

    def read(self):
        if self.cap is None:
            return False, None

        return self.cap.read()

    def stop(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def is_opened(self):
        return self.cap is not None and self.cap.isOpened()