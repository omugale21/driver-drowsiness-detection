import cv2
import mediapipe as mp
import numpy as np
import requests
import time
import os

from app.detection.drowsiness import DrowsinessDetector
from app.detection.head_pose import HeadPoseEstimator, get_attention
from app.services.alert_service import trigger_alert
from app.services.fatigue_service import FatigueScorer
from app.services.camera_service import WebcamStream
from app.services.recording_service import VideoRecorder
from app.services.behavior_service import BehaviorMonitor
from app.services.voice_service import speak_async
from app.services.screenshot_service import ScreenshotService
from app.config import *

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=False
)

drowsy_detector = DrowsinessDetector()
head_pose = HeadPoseEstimator()
fatigue_scorer = FatigueScorer()
recorder = VideoRecorder()
behavior = BehaviorMonitor()
screenshot = ScreenshotService()

cap = WebcamStream(src=0).start()

max_fatigue = 0
total_alerts = 0
start_time = time.time()

frame_count = 0
process_counter = 0

# NEW
no_face_counter = 0
NO_FACE_THRESHOLD = 15

last_behavior_alert = 0
BEHAVIOR_COOLDOWN = 5

print("Press 'q' to exit")

while True:

    frame = cap.read()
    if frame is None:
        continue

    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)

    process_counter += 1

    if process_counter % 2 != 0:
        if os.environ.get("DISPLAY"):
            cv2.imshow("Driver Monitoring", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    status = "AWAKE"
    fatigue_score = 0
    attention = "FOCUSED"

    if results.multi_face_landmarks:

        no_face_counter = 0

        for face_landmarks in results.multi_face_landmarks:

            h, w, _ = frame.shape

            points = np.array([
                (int(lm.x * w), int(lm.y * h))
                for lm in face_landmarks.landmark
            ])

            status, ear, mar, _ = drowsy_detector.process(points)

            pitch, yaw, roll = head_pose.estimate(frame, points)
            attention = get_attention(pitch, yaw, head_pose, points, frame.shape)

            fatigue_score = fatigue_scorer.update(status, attention, mar)

            max_fatigue = max(max_fatigue, fatigue_score)

            if fatigue_score > FATIGUE_WARNING:
                total_alerts += 1

            trigger_alert(fatigue_score, attention)

            is_distracted = behavior.check_distraction(attention)
            is_microsleep = behavior.check_microsleep(status)

            current_time = time.time()

            if is_distracted and (current_time - last_behavior_alert > BEHAVIOR_COOLDOWN):
                speak_async("Driver distracted")
                last_behavior_alert = current_time

            if is_microsleep and (current_time - last_behavior_alert > BEHAVIOR_COOLDOWN):
                speak_async("Micro sleep detected")
                last_behavior_alert = current_time

            if RECORDING_ENABLED and fatigue_score > FATIGUE_CRITICAL:
                recorder.start(frame)
                recorder.write(frame)
            else:
                recorder.stop()

            if SCREENSHOT_ENABLED and fatigue_score > FATIGUE_SCREENSHOT:
                screenshot.capture(frame)

            if fatigue_score < 40:
                color = (0, 255, 0)
            elif fatigue_score < 60:
                color = (0, 255, 255)
            else:
                color = (0, 0, 255)

            display_attention = "FOCUSED" if attention == "FOCUSED" else "DISTRACTED"

            cv2.putText(frame, f"Status: {status}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

            cv2.putText(frame, f"Attention: {display_attention}", (20, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

            cv2.putText(frame, f"Score: {fatigue_score}", (20, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    else:
        no_face_counter += 1

        if no_face_counter > NO_FACE_THRESHOLD:
            status = "NO_FACE"
            attention = "DISTRACTED"
            fatigue_score = 80

            trigger_alert(fatigue_score, attention)

            cv2.putText(frame, "FACE NOT VISIBLE!", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    frame_count += 1

    if frame_count % 10 == 0:
        _, jpeg = cv2.imencode('.jpg', frame)

        try:
            requests.post("http://flask:5000/update_frame", data=jpeg.tobytes(), timeout=0.2)
        except:
            pass

        try:
            requests.post("http://flask:5000/update_status", json={
                "status": status,
                "attention": attention,
                "fatigue_score": fatigue_score
            }, timeout=0.2)
        except:
            pass

    if os.environ.get("DISPLAY"):
        cv2.imshow("Driver Monitoring", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.stop()
cv2.destroyAllWindows()