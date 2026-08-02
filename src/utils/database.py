import sqlite3

DATABASE_PATH = "database/surveillance.db"


def create_connection():
    return sqlite3.connect(DATABASE_PATH)


def create_table():

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detections(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        object_class TEXT NOT NULL,
        confidence REAL NOT NULL,
        snapshot_path TEXT

    )
    """)

    connection.commit()
    connection.close()


def insert_detection(timestamp, object_class, confidence, snapshot_path):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO detections
    (timestamp, object_class, confidence, snapshot_path)

    VALUES (?, ?, ?, ?)
    """,
    (
        timestamp,
        object_class,
        confidence,
        snapshot_path
    ))

    connection.commit()
    connection.close()


def fetch_all_detections():

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM detections")

    rows = cursor.fetchall()

    connection.close()

    return rows