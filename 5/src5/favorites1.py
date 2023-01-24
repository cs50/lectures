import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("<tr>")
        print(" " * 4 + "<td>" + row["Timestamp"] + "</td>")
        print(" " * 4 + "<td>" + row["title"] + "</td>")
        print(" " * 4 + "<td>")
        genres = row["genres"].split(", ")
        for genre in genres:
            print(" " * 8 + "<span class='badge text-bg-primary'>" + genre + "</span>")
        print(" " * 4 + "</td>")
        print("</tr>")
