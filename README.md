# Gmail Automation System

An intelligent Gmail automation system that reads, classifies, and summarizes emails using machine learning and OCR capabilities.

## Features

- **Email Reading**: Automatically reads emails from inbox and spam folders using IMAP
- **Spam Detection**: ML-based spam detection using Naive Bayes classifier
- **Email Summarization**: Automatic summarization of email content and attachments
- **Attachment Handling**: Extracts and processes email attachments
- **OCR Support**: Reads text from images and PDFs using Tesseract OCR
- **Web Dashboard**: Flask-based dashboard for viewing email analytics
- **Read/Unread Status**: Accurate tracking of email read status

## Tech Stack

- **Python**: Core programming language
- **FastAPI**: Web framework (for API endpoints)
- **Flask**: Web dashboard framework
- **Scikit-learn**: Machine learning for spam detection
- **Tesseract OCR**: Optical character recognition for images and PDFs
- **IMAP**: Email protocol for reading Gmail
- **Pillow**: Image processing library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Bishwaprotapi/gmail_automation
cd gmail_automation
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file with your Gmail credentials:
```
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
IMAP_SERVER=imap.gmail.com
```

## Usage

Run the main script to start email processing:
```bash
python main.py
```

To start the web dashboard:
```bash
python dashboard/app.py
```

## Project Structure

```
gmail_automation/
├── main.py                 # Entry point
├── gmail_reader.py         # Email reading logic
├── ml_classifier.py        # ML-based classification
├── spam_detector.py        # Spam detection
├── summarizer.py           # Email summarization
├── attachment_handler.py   # Attachment processing
├── ocr_reader.py           # OCR functionality
├── csv_manager.py          # CSV data management
├── config.py               # Configuration settings
├── utils.py                # Utility functions
├── dashboard/              # Web dashboard
├── data/                   # Training data and database
├── downloads/              # Downloaded attachments
└── requirements.txt        # Python dependencies
```

## Author

**Bishwaprotap Ray**  
**Role**: Software Developer Intern | AI & Machine Learning Engineer  
**Education**: B.Sc. in Computer Science & Engineering (International University of Business Agriculture and Technology)  
**Specialization**: AI, Machine Learning, LLM, FastAPI, Voice Assistant Development  
**Location**: Dhaka, Bangladesh  

### Contact

- **Mobile**: +8801788974534
- **Email**: baburay214@gmail.com
- **LinkedIn**: [https://www.linkedin.com/in/bishwaprotap-ray/](https://www.linkedin.com/in/bishwaprotap-ray/)
- **GitHub**: [https://github.com/Bishwaprotapi](https://github.com/Bishwaprotapi)

## License

This project is open source and available under the MIT License.
