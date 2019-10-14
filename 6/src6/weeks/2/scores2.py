# Generates a bar chart of three scores using a list

from cs50 import get_int


def main():

    # Get scores from user
    scores = []
    for i in range(3):
        scores.append(get_int(f"Score {i + 1}: "))

    # Chart scores
    for i in range(len(scores)):
        print(f"Score {i + 1}: ", end="")
        chart(scores[i])

def chart(score):
    """Generate bar"""

    # Output one hash per point
    for i in range(score):
        print("#", end="")
    print()


if __name__ == "__main__":
    main()
