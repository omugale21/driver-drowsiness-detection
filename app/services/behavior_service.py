import time
from app.config import DISTRACTION_TIME, MICROSLEEP_TIME


class BehaviorMonitor:
    def __init__(self):
        self.distraction_start = None
        self.drowsy_start = None

    def check_distraction(self, attention):
        if attention != "FOCUSED":
            if self.distraction_start is None:
                self.distraction_start = time.time()

            duration = time.time() - self.distraction_start

            if duration > DISTRACTION_TIME:
                return True
        else:
            self.distraction_start = None

        return False

    def check_microsleep(self, status):
        if status == "DROWSY":
            if self.drowsy_start is None:
                self.drowsy_start = time.time()

            duration = time.time() - self.drowsy_start

            if duration > MICROSLEEP_TIME:
                return True
        else:
            self.drowsy_start = None

        return False