#include <cs50.h>
#include <stdio.h>

int square(int n);

int main(void)
{
    printf("x is ");
    int x = get_int();
    printf("x^2 is %i\n", square(x));
}

int square(int n)
{
    return n * n;
}
