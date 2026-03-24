class FatigueScorer:
    def __init__(self):
        self.score = 0
        self.smoothing_factor = 0.8

    def update(self, status, attention, mar):

        temp_score = self.score

        if status == "DROWSY":
            temp_score += 10
        else:
            temp_score -= 2

        if mar > 0.7:
            temp_score += 10

        if attention != "FOCUSED":
            temp_score += 5
        else:
            temp_score -= 2

        temp_score = max(0, min(100, temp_score))

        self.score = int(
            self.smoothing_factor * self.score +
            (1 - self.smoothing_factor) * temp_score
        )

        return self.score

    def get_state(self):
        if self.score < 30:
            return "NORMAL"
        elif self.score < 60:
            return "WARNING"
        else:
            return "CRITICAL"