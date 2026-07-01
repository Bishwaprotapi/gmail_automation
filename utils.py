from email.utils import parsedate_to_datetime


def split_date(date_str):
    try:
        dt = parsedate_to_datetime(date_str)

        # 🔥 FORMAT FIX
        date = dt.strftime("%d-%b-%y")   # 07-Apr-26
        time = dt.strftime("%H:%M:%S")

        return date, time

    except:
        return "", ""