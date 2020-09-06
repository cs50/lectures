// Prints a square of bricks, sized as specified by user

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for a positive number
    int n;
    do
    {
        n = get_int("Positive number: ");
    }
    while (n <= 0);

    // Print out this many rows
    for (int i = 0; i < n; i++)
    {
        // Print out this many columns
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
