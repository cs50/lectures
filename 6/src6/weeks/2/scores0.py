# Generates a bar chart of three scores

from cs50 import get_int

# Get scores from user
score1 = get_int("Score 1: ")
score2 = get_int("Score 2: ")
score3 = get_int("Score 3: ")

# Generate first bar
print("Score 1: ", end="");
for i in range(score1):
    print("#", end="")
print()

# Generate second bar
print("Score 2: ", end="");
for i in range(score2):
    print("#", end="")
print()

# Generate third bar
print("Score 3: ", end="");
for i in range(score3):
    print("#", end="")
print()
