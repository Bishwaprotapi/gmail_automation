import re

def clean_text(text):
    if not text:
        return ""

    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'http\S+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9.,% ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def extract_sentences(text):
    sentences = re.split(r'[.!?]', text)

    result = []
    for s in sentences:
        s = s.strip()
        if len(s) > 30 and "utm_" not in s:
            result.append(s)

    return result[:5]


def summarize(subject, body, attachment_text):
    # ✅ STACK EVERYTHING
    combined = f"{subject}. {body}. {attachment_text}"

    text = clean_text(combined)

    if not text:
        return ""

    sentences = extract_sentences(text)

    if len(sentences) < 3:
        return "\n".join(sentences)

    s1 = sentences[0]
    s2 = sentences[1]
    s3 = sentences[2]

    # ✅ AI STYLE OUTPUT
    return (
        f"{s1}.\n"
        f"{s2}.\n"
        f"Overall, {s3.lower()}."
    )