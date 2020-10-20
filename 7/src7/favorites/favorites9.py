# Searches CSV for popularity of a title

import csv

from cs50 import SQL

# Open database
db = SQL("sqlite:///shows.db")

# Prompt user for title
title = input("Title: ").strip().upper()

# Search for title
rows = db.execute("SELECT COUNT(*) AS counter FROM shows WHERE title = ?", title)

# Print popularity
print(rows[0]["counter"])
