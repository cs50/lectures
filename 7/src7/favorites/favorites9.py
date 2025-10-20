# Sorts favorites by value using SQL

from cs50 import SQL

# Open database
db = SQL("sqlite:///favorites.db")

# Search for title
rows = db.execute("SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC")

# Print popularity
for row in rows:
    print(row["language"], row["n"])
