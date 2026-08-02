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
# Save Changes
# ============================================
connection.commit()

# ============================================
# Close Database
# ============================================
connection.close()

print("Database Closed.")