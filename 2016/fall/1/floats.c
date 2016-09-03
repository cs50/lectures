#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prompt user for x
    printf("x is ");
    float x = get_float();
    
    // prompt user for y
    printf("y is ");
    float y = get_float();
    
    // perform division for user
    printf("%f divided by %f is %f\n", x, y, x / y);
}