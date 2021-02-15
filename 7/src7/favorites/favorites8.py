# Imports titles and genres from CSV into a SQLite database

import cs50
import csv

# Create database
open("shows.db", "w").close()
db = cs50.SQL("sqlite:///shows.db")

# Create tables
db.execute("CREATE TABLE shows (id INTEGER, title TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE genres (show_id INTEGER, genre TEXT, FOREIGN KEY(show_id) REFERENCES shows(id))")

# Open CSV file
with open("Favorite TV Shows - Form Responses 1.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file
    for row in reader:

        # Canoncalize title
        title = row["title"].strip().upper()

        # Insert title
        id = db.execute("INSERT INTO shows (title) VALUES(?)", title)

        # Insert genres
        for genre in row["genres"].split(", "):
            db.execute("INSERT INTO genres (show_id, genre) VALUES(?, ?)", id, genre)
