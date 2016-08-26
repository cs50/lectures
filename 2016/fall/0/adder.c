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
    
    // calculate sum for user
    printf("sum is %i\n", x + y);
}