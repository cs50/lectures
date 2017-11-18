// Prints a positive number of question marks, as specified by user

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

    // Print out that many bricks
    for (int i = 0; i < n; i++)
    {
        printf("#\n");
    }
}
