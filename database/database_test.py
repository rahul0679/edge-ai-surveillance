import sqlite3

# ============================================
# Connect to Database
# ============================================
connection = sqlite3.connect("database/surveillance.db")

print("Database Connected Successfully!")

# ============================================
# Create Cursor
# ============================================
cursor = connection.cursor()

# ============================================
# Create Table
# ============================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS detections (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp TEXT NOT NULL,

    object_class TEXT NOT NULL,

    confidence REAL NOT NULL,

    snapshot_path TEXT

)
""")

print("Table Created Successfully!")
# ============================================
# Insert Data
# ============================================
cursor.execute("""
INSERT INTO detections
(timestamp, object_class, confidence, snapshot_path)

VALUES (?, ?, ?, ?)
""",
(
    "2026-08-02 18:25:30",
    "person",
    0.94,
    "snapshots/test.jpg"
))
# ============================================
# Select Data
# ============================================
cursor.execute("SELECT * FROM detections")

rows = cursor.fetchall()

# Print Retrieved Data

print("\nDetection Logs")
print("-" * 50)

for row in rows:

    id = row[0]
    timestamp = row[1]
    object_class = row[2]
    confidence = row[3]
    snapshot = row[4]

    print(f"ID         : {id}")
    print(f"Timestamp  : {timestamp}")
    print(f"Object     : {object_class}")
    print(f"Confidence : {confidence}")
    print(f"Snapshot   : {snapshot}")
    print("-" * 40)

# ============================================
# Save Changes
# ============================================
connection.commit()

# ============================================
# Close Database
# ============================================
connection.close()

print("Database Closed.")