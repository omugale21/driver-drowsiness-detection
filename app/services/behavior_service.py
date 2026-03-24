class BehaviorMonitor:
    def __init__(self):
        self.distraction_counter = 0
        self.microsleep_counter = 0

        self.DISTRACTION_THRESHOLD = 15
        self.MICROSLEEP_THRESHOLD = 10

    def check_distraction(self, attention):
        if attention != "FOCUSED":
            self.distraction_counter += 1
        else:
            self.distraction_counter = 0

        return self.distraction_counter > self.DISTRACTION_THRESHOLD

    def check_microsleep(self, status):
        if status == "DROWSY":
            self.microsleep_counter += 1
        else:
            self.microsleep_counter = 0

        return self.microsleep_counter > self.MICROSLEEP_THRESHOLD