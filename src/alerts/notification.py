from plyer import notification


def show_notification(object_name, confidence):
    notification.notify(
        title="⚠️ Edge AI Surveillance",
        message=(
            f"Threat Detected!\n\n"
            f"Object: {object_name}\n"
            f"Confidence: {confidence:.2f}"
        ),
        timeout=5
    )