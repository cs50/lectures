import cs50
import csv

# Create database
open("shows4.db", "w").close()
db = cs50.SQL("sqlite:///shows4.db")

# Create tables
db.execute("CREATE TABLE shows (id INT, title TEXT, year NUMERIC, PRIMARY KEY(id))")
db.execute("CREATE TABLE genres (show_id INT, genre TEXT, FOREIGN KEY(show_id) REFERENCES shows(id))")

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

                    # Trim prefix from tconst
                    id = int(row["tconst"][2:])

                    # Insert show
                    db.execute("INSERT INTO shows (id, title, year) VALUES(?, ?, ?)", id, row["primaryTitle"], startYear)

                    # Insert genres
                    if row["genres"] != "\\N":
                        for genre in row["genres"].split(","):
                            db.execute("INSERT INTO genres (show_id, genre) VALUES(?, ?)", id, genre)

