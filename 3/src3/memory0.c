// Indexes beyond end of an array

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get scores from user
    int scores[3];
    for (int i = 0; i <= 3; i++)
    {
        scores[i] = get_int("Score: ");
    }

    // Generate bars
    for (int i = 0; i <= 3; i++)
    {
        printf("Score %i: ", i);
        for (int i = 0; i < scores[i]; i++)
        {
            printf("#");
        }
        printf("\n");
    }
}
