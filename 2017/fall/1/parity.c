// Demonstrates remainder operation.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prompt user for integer
    int n = get_int("n: ");

    // check parity of integer
    if (n % 2 == 0)
    {
        printf("even\n");
    }
    else
    {
        printf("odd\n");
    }
}
