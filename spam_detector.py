from ml_classifier import predict

SPAM_KEYWORDS = [
    "win", "free", "offer", "lottery", "urgent",
    "prize", "click", "buy now", "limited"
]


def detect_spam(subject, body, folder):
    text = (subject + " " + body).lower()

    # ✅ 1. Gmail spam folder = spam
    if folder.lower() == "[gmail]/spam":
        return "Spam"

    # ✅ 2. ML prediction
    ml_result = predict(text)

    # ✅ 3. keyword score (count)
    keyword_count = sum(1 for word in SPAM_KEYWORDS if word in text)

    # 🔥 SMART LOGIC
    if ml_result == "spam" and keyword_count >= 1:
        return "Spam"

    if keyword_count >= 3:
        return "Spam"

    return "Authentic"