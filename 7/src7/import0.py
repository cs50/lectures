import csv

# Open TSV file
# https://datasets.imdbws.com/title.basics.tsv.gz
with open("title.basics.tsv", "r") as titles:

    # Create DictReader
    reader = csv.DictReader(titles, delimiter="\t")

    # Open CSV file
    with open("shows0.csv", "w") as shows:

        # Create writer
        writer = csv.writer(shows)

        # Write header
        writer.writerow(["tconst", "primaryTitle", "startYear", "genres"])

        # Iterate over TSV file
        for row in reader:

            # If non-adult TV show
            if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

                # Write row
                writer.writerow([row["tconst"], row["primaryTitle"], row["startYear"], row["genres"]])
