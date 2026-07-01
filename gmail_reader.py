import imaplib
import email
from email.header import decode_header

from config import *
from spam_detector import detect_spam
from summarizer import summarize
from attachment_handler import save_attachments
from utils import split_date
from csv_manager import save_batch
from ml_classifier import train_model


def decode(val):
    if isinstance(val, bytes):
        return val.decode(errors="ignore")
    return val or ""


# ✅ FIXED (Accurate Read/Unread)
def get_read_status(mail, num):
    try:
        typ, response = mail.fetch(num, "(FLAGS)")
        if typ != "OK":
            return "Unread"

        flags = response[0].decode()

        # 🔥 strict check
        if "\\Seen" in flags:
            return "Read"
        return "Unread"

    except:
        return "Unread"


def extract_body(msg):
    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            ct = part.get_content_type()

            if ct == "text/plain":
                payload = part.get_payload(decode=True)
                if payload:
                    return payload.decode(errors="ignore")

            elif ct == "text/html" and not body:
                payload = part.get_payload(decode=True)
                if payload:
                    body = payload.decode(errors="ignore")
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode(errors="ignore")

    return body


def process_mailbox(mail, folder):
    mail.select(folder)
    _, data = mail.search(None, "ALL")

    ids = data[0].split()
    print(f"📂 Processing {folder} - {len(ids)} emails")

    for i in range(0, len(ids), BATCH_SIZE):
        batch_ids = ids[i:i+BATCH_SIZE]
        batch_data = []

        for num in batch_ids:
            try:
                _, msg_data = mail.fetch(num, "(RFC822)")
                msg = email.message_from_bytes(msg_data[0][1])

                subject, _ = decode_header(msg["Subject"])[0]
                subject = decode(subject)

                sender = decode(msg.get("From"))
                date, time = split_date(msg.get("Date"))

                body = extract_body(msg)

                # ✅ FIXED READ STATUS
                read_status = get_read_status(mail, num)

                # ✅ spam logic fix
                spam_status = detect_spam(subject, body, folder)

                attachments = [p for p in msg.walk() if p.get_filename()]
                has_attach, attach_text = save_attachments(sender, attachments)

                summary = summarize(subject, body, attach_text)

                batch_data.append({
                    "sender": sender,
                    "subject": subject,
                    "body": body[:200],
                    "date": date,
                    "time": time,
                    "read": read_status,
                    "spam": spam_status,
                    "summary": summary,
                    "attachment": "Yes" if has_attach else "No"
                })

            except Exception as e:
                print("⚠️ Error:", e)

        save_batch(batch_data)
        print(f"✅ Batch {i} → {i+len(batch_ids)} saved")


def read_emails():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)

    train_model()

    process_mailbox(mail, "inbox")
    process_mailbox(mail, "[Gmail]/Spam")

    print("🎉 DONE")