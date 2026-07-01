import csv
import os

FILE = "data/database.csv"

def save_batch(emails):
    os.makedirs("data", exist_ok=True)
    file_exists = os.path.isfile(FILE)

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "Sender", "Subject", "Body", "Date", "Time",
                "Read/Unread", "Spam/Authentic", "Summary", "Attachment"
            ])

        for e in emails:
            writer.writerow([
                e["sender"], e["subject"], e["body"],
                e["date"], e["time"], e["read"],
                e["spam"], e["summary"], e["attachment"]
            ])