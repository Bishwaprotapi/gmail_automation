import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

IMAP_SERVER = "imap.gmail.com"

# batch size (performance control)
BATCH_SIZE = 250
MAX_FOLDER_NAME = 25
MAX_FILE_NAME = 40