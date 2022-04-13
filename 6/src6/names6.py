# Reads from a file, one line at a time

with open("names.txt") as file:
    for line in file:
        print("hello,", line.rstrip())
