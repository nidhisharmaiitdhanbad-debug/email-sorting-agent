import csv

from agents.parser_agent import parse_email
from agents.classification_agent import classify_email
from agents.priority_agent import assign_priority


with open("data/emails.csv", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        subject = row["subject"]
        body = row["body"]

        text = parse_email(subject, body)

        category = classify_email(text)

        priority = assign_priority(text)

        print("EMAIL:", subject)
        print("Category:", category)
        print("Priority:", priority)
        print("---------------------")
