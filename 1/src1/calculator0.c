// Addition with int

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("What's x? ");

    // Prompt user for y
    int y = get_int("What's y? ");

    // Add numbers
    int z = x + y;

    // Perform addition
    printf("%i\n", z);
}
