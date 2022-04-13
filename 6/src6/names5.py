# Reads from a file

with open("names.txt") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
