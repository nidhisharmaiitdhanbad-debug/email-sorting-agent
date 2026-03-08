def parse_email(subject, body):
    """
    Simple parser agent that cleans email text
    """

    text = (subject + " " + body).lower().strip()

    return text
