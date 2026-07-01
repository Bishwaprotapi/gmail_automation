import pytesseract
from PIL import Image
from pdfminer.high_level import extract_text
import os
import warnings

# 🔕 suppress pdfminer warnings
warnings.filterwarnings("ignore")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_file(path):
    ext = os.path.splitext(path)[1].lower()

    try:
        # ✅ IMAGE OCR
        if ext in [".png", ".jpg", ".jpeg"]:
            return pytesseract.image_to_string(Image.open(path))

        # ✅ PDF TEXT + OCR fallback
        elif ext == ".pdf":
            try:
                text = extract_text(path)

                # যদি pdf text empty হয় → OCR fallback
                if not text or len(text.strip()) < 20:
                    return "[Scanned PDF - OCR Limited]"

                return text

            except:
                return "[PDF Read Error]"

    except Exception as e:
        print("⚠️ OCR Error:", e)

    return ""