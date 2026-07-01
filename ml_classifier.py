import os
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

MODEL = None


def load_training_data():
    texts = []
    labels = []

    path = "data/training_data.csv"

    if not os.path.exists(path):
        return [], []

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            texts.append(row["text"])
            labels.append(row["label"])

    return texts, labels


def train_model():
    global MODEL

    texts, labels = load_training_data()

    if not texts:
        MODEL = None
        return

    MODEL = Pipeline([
        ("vectorizer", CountVectorizer()),
        ("classifier", MultinomialNB())
    ])

    MODEL.fit(texts, labels)


def predict(text):
    if MODEL is None:
        return "unknown"

    return MODEL.predict([text])[0]