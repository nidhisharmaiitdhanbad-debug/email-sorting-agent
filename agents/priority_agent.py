def assign_priority(text):

    if "urgent" in text or "deadline" in text:
        return "High"

    elif "offer" in text or "discount" in text:
        return "Low"

    else:
        return "Medium"
