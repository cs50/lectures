// Generates a bar chart of three scores

#include <cs50.h>
#include <stdio.h>

void chart(int score);

int main(void)
{
    // Get scores from user
    int score1 = get_int("Score 1: ");
    int score2 = get_int("Score 2: ");
    int score3 = get_int("Score 3: ");

    // Chart first score
    printf("Score 1: ");
    chart(score1);

    // Chart second score
    printf("Score 2: ");
    chart(score2);

    // Chart third score
    printf("Score 3: ");
    chart(score3);
}

// Generate bar
void chart(int score)
{
    // Output one hash per point
    for (int i = 0; i < score; i++)
    {
        printf("#");
    }
    printf("\n");
}
