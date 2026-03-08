def classify_email(text):

    if "meeting" in text or "project" in text:
        return "Work"

    elif "party" in text or "dinner" in text:
        return "Personal"

    elif "offer" in text or "free" in text:
        return "Spam"

    else:
        return "General"
