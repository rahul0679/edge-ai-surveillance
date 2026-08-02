from playsound import playsound
import threading
import os

# Alarm file path
ALARM_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "assets",
        "sounds",
        "alarm.wav"
    )
)

def play_alarm():
    def sound():
        try:
            playsound(ALARM_PATH)
        except Exception as e:
            print(f"Alarm Error: {e}")

    threading.Thread(target=sound, daemon=True).start()