class FatigueScorer:
    def __init__(self):
        self.score = 0

    def update(self, status, attention, mar):

        # -------------------------------
        # Drowsiness
        # -------------------------------
        if status == "DROWSY":
            self.score += 10
        else:
            self.score -= 3

        # -------------------------------
        # Yawning
        # -------------------------------
        if mar > 0.7:
            self.score += 15

        # -------------------------------
        # Attention
        # -------------------------------
        if attention != "FOCUSED":
            self.score += 5
        else:
            self.score -= 2

        # -------------------------------
        # Clamp score (0–100)
        # -------------------------------
        self.score = max(0, min(100, self.score))

        return self.score

    def get_state(self):
        if self.score < 30:
            return "NORMAL"
        elif self.score < 60:
            return "WARNING"
        else:
            return "CRITICAL"