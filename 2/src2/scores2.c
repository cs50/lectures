// Generates a bar chart of three scores using an array

#include <cs50.h>
#include <stdio.h>

void chart(int score);

int main(void)
{
    // Get scores from user
    int scores[3];
    for (int i = 0; i < 3; i++)
    {
        scores[i] = get_int("Score %i: ", i + 1);
    }

    // Chart scores
    for (int i = 0; i < 3; i++)
    {
        printf("Score %i: ", i + 1);
        chart(scores[i]);
    }
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
