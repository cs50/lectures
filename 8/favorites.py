import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("<tr>")
        print(" " * 4 + "<td>" + row["Timestamp"] + "</td>")
        print(" " * 4 + "<td>" + row["language"] + "</td>")
        print(" " * 4 + "<td>" + row["problem"] + "</td>")
        print("</tr>")
