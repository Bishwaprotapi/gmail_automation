from flask import Flask, render_template, request
import csv

app = Flask(__name__)

DATA_FILE = "../data/database.csv"


def load_data():
    data = []

    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except:
        pass

    return data


@app.route("/")
def index():
    q = request.args.get("q", "").lower()
    status = request.args.get("status", "")
    spam = request.args.get("spam", "")
    attach = request.args.get("attach", "")

    emails = load_data()

    # 🔍 Search
    if q:
        emails = [
            e for e in emails
            if q in e["Sender"].lower() or q in e["Subject"].lower()
        ]

    # 🎯 Filter
    if status:
        emails = [e for e in emails if e["Read/Unread"] == status]

    if spam:
        emails = [e for e in emails if e["Spam/Authentic"] == spam]

    if attach:
        emails = [e for e in emails if e["Attachment"] == attach]

    # 🔥 SORT BY DATE + TIME (LATEST FIRST)
    try:
        emails = sorted(
            emails,
            key=lambda x: (x["Date"], x["Time"]),
            reverse=True
        )
    except:
        pass

    return render_template("index.html", emails=emails)


if __name__ == "__main__":
    app.run(debug=True)