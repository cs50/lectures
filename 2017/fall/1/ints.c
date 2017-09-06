#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prompt user for x
    printf("x is ");
    int x = get_int();
    
    // prompt user for y
    printf("y is ");
    int y = get_int();
    
    // perform calculations for user
    printf("%i plus %i is %i\n", x, y, x + y);
    printf("%i minus %i is %i\n", x, y, x - y);
    printf("%i times %i is %i\n", x, y, x * y);
    printf("%i divided by %i is %i\n", x, y, x / y);
    printf("remainder of %i divided by %i is %i\n", x, y, x % y);
}