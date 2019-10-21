# Emails students

import csv
import os
import smtplib
import sys

# Log into email server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))

# Email each student
with open("Sorting Hat - Form Responses 1.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name = row[1]
        email = row[2]
        house = row[3]
        message = f"You are in {house}, {name}!"
        server.sendmail(os.getenv("SENDER"), email, message)
        print(".", end="")
print()
