// Doubles a number

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("x: ");

    // Double it
    printf("%i\n", x * 2);
}
