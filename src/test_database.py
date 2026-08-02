from utils.database import *

create_table()

insert_detection(
    "2026-08-02 19:00:00",
    "person",
    0.94,
    "snapshots/test.jpg"
)

rows = fetch_all_detections()

for row in rows:
    print(row)