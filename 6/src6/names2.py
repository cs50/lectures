# Writes to a file

name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()
