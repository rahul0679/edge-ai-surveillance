import winsound
import threading


def play_alarm():
    """
    Plays a short emergency alarm.
    Runs in a separate thread so the GUI does not freeze.
    """

    def alarm_sound():

        for _ in range(3):
            winsound.Beep(1200, 300)
            winsound.Beep(800, 300)

    threading.Thread(
        target=alarm_sound,
        daemon=True
    ).start()