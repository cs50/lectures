import cs50
import csv

# Create database
open(f"shows3.db", "w").close()
db = cs50.SQL(f"sqlite:///shows3.db")

# Create table
db.execute("CREATE TABLE shows (tconst TEXT, primaryTitle TEXT, startYear NUMERIC, genres TEXT)")

# Open TSV file
with open("title.basics.tsv", "r") as input:

    # Create DictReader
    reader = csv.DictReader(input, delimiter="\t")

    # Iterate over TSV file
    for row in reader:

        # If non-adult TV show
        if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

            # If year not missing
            if row["startYear"] != "\\N":

                # Remove \N from genres
                genres = row["genres"] if row["genres"] != "\\N" else None

                # If since 1970
                startYear = int(row["startYear"])
                if startYear >= 1970:

                    # Insert row
                    db.execute("INSERT INTO shows (tconst, primaryTitle, startYear, genres) VALUES(?, ?, ?, ?)",
                               row["tconst"], row["primaryTitle"], startYear, genres)
