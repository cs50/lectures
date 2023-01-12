import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("<tr>")
        print(" " * 4 + "<td>" + row["Timestamp"] + "</td>")
        print(" " * 4 + "<td>" + row["title"] + "</td>")
        print(" " * 4 + "<td>" + row["genres"] + "</td>")
        print("</tr>")
