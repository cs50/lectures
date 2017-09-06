// Demonstrates integer arithmetic.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prompt user for x
    int x = get_int("x: ");

    // prompt user for y
    int y = get_int("y: ");

    // perform arithmetic
    printf("%i plus %i is %i\n", x, y, x + y);
    printf("%i minus %i is %i\n", x, y, x - y);
    printf("%i times %i is %i\n", x, y, x * y);
    printf("%i divided by %i is %i\n", x, y, x / y);
    printf("remainder of %i divided by %i is %i\n", x, y, x % y);
}
