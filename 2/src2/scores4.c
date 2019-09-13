// Generates a bar chart of three scores by passing an array, using a constant

#include <cs50.h>
#include <math.h>
#include <stdio.h>

const int COUNT = 3;

void chart(int count, int scores[]);

int main(void)
{
    // Get scores from user
    int scores[COUNT];
    for (int i = 0; i < COUNT; i++)
    {
        scores[i] = get_int("Score %i: ", i + 1);
    }

    // Chart scores
    chart(COUNT, scores);
}

// Generate bars
void chart(int count, int scores[])
{
    // Output one hash per point
    for (int i = 0; i < count; i++)
    {
        for (int j = 0; j < scores[i]; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
