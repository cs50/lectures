# Averages three numbers using an array and a loop

from cs50 import get_int

# Get scores
scores = []
for i in range(3):
    scores.append(get_int("Score: "))

# Print average
print(f"Average: {sum(scores) / len(scores)}")
