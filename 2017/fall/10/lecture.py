import sys

from cs50 import SQL

db = SQL("sqlite:///lecture.db")

# Query database for all albums
rows = db.execute("SELECT * FROM Album WHERE Title = :t", t=sys.argv[1])

# For each album in database
for row in rows:

    # Print title of album
    print(row["Title"])
