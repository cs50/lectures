// Floating-point arithmetic with double

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    double x = get_double("x: ");

    // Prompt user for y
    double y = get_double("y: ");

    // Perform division
    printf("x / y = %.50f\n", x / y);
}
