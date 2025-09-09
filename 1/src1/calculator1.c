// Addition with int, without third variable

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("What's x? ");

    // Prompt user for y
    int y = get_int("What's y? ");

    // Perform addition
    printf("%i\n", x + y);
}
