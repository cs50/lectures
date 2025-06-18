# Demonstrates indexing into a dict

schools = {
    "Harvard": "Cambridge",
    "MIT": "Cambridge",
    "Oxford": "Oxford",
}

for school in schools:
    print(school, schools[school], sep=" is in ")
