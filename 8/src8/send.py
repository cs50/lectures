# Emails class

import csv
import os
import smtplib
import sys

from email.message import EmailMessage

# Log into email server
server = smtplib.SMTP(os.getenv("HOST"), os.getenv("PORT"))
server.starttls()
server.login(os.getenv("USER"), os.getenv("PASSWORD"))

# Open CSV file
with open("responses.csv", "r") as file:

    # Iterate over CSV file
    reader = csv.DictReader(file)
    for row in reader:

        # Prepare message
        message = EmailMessage()
        message["from"] = os.getenv("FROM")
        message["to"] = row["email"]
        message["subject"] = "Test Review"
        message.set_content(f"Hi {row['first name']},\n\nhttps://youtu.be/oHg5SJYRHA0\n\nAll the best,\nBrian")

        # Send message
        server.send_message(message)
        print(".", end="")

print()
