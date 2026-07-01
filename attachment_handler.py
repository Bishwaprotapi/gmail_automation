import os
import re
from datetime import datetime
from email.header import decode_header
from ocr_reader import extract_text_from_file


def decode_text(value):
    try:
        parts = decode_header(value)
        decoded = ""
        for part, enc in parts:
            if isinstance(part, bytes):
                decoded += part.decode(enc or "utf-8", errors="ignore")
            else:
                decoded += part
        return decoded
    except:
        return "file"


def safe_name(name):
    base, ext = os.path.splitext(name)
    base = re.sub(r'[^a-zA-Z0-9]', '_', base)
    ext = re.sub(r'[^a-zA-Z0-9.]', '', ext)
    return (base + ext)[:60]


def save_attachments(sender, parts):
    if not parts:
        return False, ""

    sender = safe_name(decode_text(sender))[:25]

    folder = os.path.join(
        "downloads",
        f"{sender}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )

    os.makedirs(folder, exist_ok=True)

    full_text = ""

    for i, part in enumerate(parts):
        filename = part.get_filename()

        if filename:
            filename = safe_name(decode_text(filename))

            if not filename:
                filename = f"file_{i}.bin"

            path = os.path.join(folder, filename)

            try:
                with open(path, "wb") as f:
                    f.write(part.get_payload(decode=True))

                # 🔥 ALWAYS OCR / TEXT EXTRACT
                extracted = extract_text_from_file(path)

                if extracted:
                    full_text += " " + extracted

            except Exception as e:
                print("⚠️ File error:", e)

    return True, full_text