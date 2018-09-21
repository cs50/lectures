// Generates a bar chart of three scores by using an array and using a constant

#include <cs50.h>
#include <stdio.h>

const int COUNT = 3;

void chart(int score);

int main(void)
{
    // Get scores from user
    int scores[COUNT];
    for (int i = 0; i < COUNT; i++)
    {
        scores[i] = get_int("Score %i: ", i + 1);
    }

    // Chart scores
    for (int i = 0; i < COUNT; i++)
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
