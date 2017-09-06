// Floating-point arithmetic

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    printf("x is ");
    float x = get_float();

    // Prompt user for y
    printf("y is ");
    float y = get_float();

    // Perform division
    printf("%f divided by %f is %f\n", x, y, x / y);
}
