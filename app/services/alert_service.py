import os
import time
from threading import Thread
from app.services.voice_service import speak_async
from app.config import FATIGUE_WARNING, FATIGUE_CRITICAL

alarm_active = False
last_alert_time = 0

COOLDOWN = 5


def sound_alarm():
    global alarm_active
    alarm_active = True
    os.system("mpg123 alarm.mp3 > /dev/null 2>&1")
    alarm_active = False


def trigger_alert(fatigue_score, attention):
    global last_alert_time, alarm_active

    current_time = time.time()

    if current_time - last_alert_time < COOLDOWN:
        return

    # Attention alert
    if attention != "FOCUSED":
        speak_async("Please focus on the road")
        last_alert_time = current_time
        return

    # Warning
    if FATIGUE_WARNING < fatigue_score <= FATIGUE_CRITICAL:
        speak_async("You are getting tired")
        last_alert_time = current_time
        return

    # Critical
    if fatigue_score > FATIGUE_CRITICAL:
        speak_async("Wake up immediately!")

        if not alarm_active:
            Thread(target=sound_alarm, daemon=True).start()

        last_alert_time = current_time