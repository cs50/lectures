// Generates a narrower bar chart of three scores by passing an array, using a constant

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
    // Output one tenth as many hashes
    for (int i = 0; i < count; i++)
    {
        // Calculate width
        int width = (int) round((float) scores[i] / 10);

        // Generate bar
        printf("Score %i: ", i);
        for (int j = 0; j < width; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
