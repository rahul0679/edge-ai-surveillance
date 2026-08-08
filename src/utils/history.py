import sqlite3

DATABASE_PATH = "database/surveillance.db"


def fetch_detections():

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            timestamp,
            object_class,
            confidence,
            snapshot_path
        FROM detections
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows


if __name__ == "__main__":

    detections = fetch_detections()

    print("=" * 90)
    print(f"{'Timestamp':20} {'Object':15} {'Confidence':12} {'Snapshot'}")
    print("=" * 90)

    for row in detections:

        timestamp, obj, confidence, snapshot = row

        print(
            f"{timestamp:20} "
            f"{obj:15} "
            f"{confidence:<12.2f} "
            f"{snapshot}"
        )