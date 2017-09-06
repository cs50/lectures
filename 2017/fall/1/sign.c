// Demonstrates conditions and relational operators.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prompt user for number
    int i = get_int("number: ");

    // check sign of number
    if (i < 0)
    {
        printf("negative\n");
    }
    else if (i > 0)
    {
        printf("positive\n");
    }
    else
    {
        printf("zero\n");
    }
}
