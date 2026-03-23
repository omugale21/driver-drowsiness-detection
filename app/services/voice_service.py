import threading

try:
    import pyttsx3
    engine = pyttsx3.init()
    VOICE_ENABLED = True
except:
    print("[WARNING] Voice disabled (not supported in Docker)")
    VOICE_ENABLED = False


def speak(text):
    if not VOICE_ENABLED:
        return
    engine.say(text)
    engine.runAndWait()


def speak_async(text):
    if not VOICE_ENABLED:
        return
    thread = threading.Thread(target=speak, args=(text,))
    thread.start()