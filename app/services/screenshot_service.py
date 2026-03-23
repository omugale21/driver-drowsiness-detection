import cv2
import os
import time


class ScreenshotService:
    def __init__(self):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        self.last_capture_time = 0

    def capture(self, frame):
        current_time = time.time()

        if current_time - self.last_capture_time < 5:
            return

        timestamp = time.strftime("%H_%M_%S")
        filename = f"screenshots/alert_{timestamp}.jpg"

        cv2.imwrite(filename, frame)
        print(f"[INFO] Screenshot saved: {filename}")

        self.last_capture_time = current_time