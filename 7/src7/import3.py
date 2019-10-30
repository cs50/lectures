import cs50
import csv

# Create database
open("shows3.db", "w").close()
db = cs50.SQL("sqlite:///shows3.db")

# Create table
db.execute("CREATE TABLE shows (tconst TEXT, primaryTitle TEXT, startYear NUMERIC, genres TEXT)")

# Open TSV file
# https://datasets.imdbws.com/title.basics.tsv.gz
with open("title.basics.tsv", "r") as titles:

    # Create DictReader
    reader = csv.DictReader(titles, delimiter="\t")

    # Iterate over TSV file
    for row in reader:

        # If non-adult TV show
        if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

            # If year not missing
            if row["startYear"] != "\\N":

                # If since 1970
                startYear = int(row["startYear"])
                if startYear >= 1970:

                    # Remove \N from genres
                    genres = row["genres"] if row["genres"] != "\\N" else None

                    # Insert show
                    db.execute("INSERT INTO shows (tconst, primaryTitle, startYear, genres) VALUES(?, ?, ?, ?)",
                               row["tconst"], row["primaryTitle"], startYear, genres)
