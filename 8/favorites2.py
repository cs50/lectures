import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("<tr>")
        print(" " * 4 + "<td>" + row["title"] + "</td>")
        print(" " * 4 + "<td>")
        for genre in row["genres"].split(", "):
            print(" " * 8 + f'<span class="badge rounded-pill bg-primary">{genre}</span>')
        print(" " * 4 + "</td>")
        print("</tr>")
