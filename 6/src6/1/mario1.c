// Prints a column of n bricks with a loop

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get positive height from user
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // Print column of bricks
    for (int i = 0; i < n; i++)
    {
        printf("#\n");
    }
}
