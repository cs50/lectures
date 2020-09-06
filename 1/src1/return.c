// Return value

#include <cs50.h>
#include <stdio.h>

int square(int n);

int main(void)
{
    int x = get_int("x: ");
    printf("%i\n", square(x));
}

// Return square of n
int square(int n)
{
    return n * n;
}
