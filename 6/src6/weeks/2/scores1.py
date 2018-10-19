# Generates a bar chart of three scores

from cs50 import get_int


def main():

    # Get scores from user
    score1 = get_int("Score 1: ")
    score2 = get_int("Score 2: ")
    score3 = get_int("Score 3: ")

    # Chart first score
    print("Score 1: ", end="")
    chart(score1)

    # Chart second score
    print("Score 2: ", end="")
    chart(score2)

    # Chart third score
    print("Score 3: ", end="")
    chart(score3)


def chart(score):

    # Output one hash per point
    for i in range(score):
        print("#", end="")
    print()


if __name__ == "__main__":
    main()
