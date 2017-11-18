// Buggy example for debug50

#include <cs50.h>
#include <stdio.h>

int get_negative_int();

int main(void)
{
    int i = get_negative_int();
    printf("%i\n", i);
}

int get_negative_int(void)
{
    int n;
    do
    {
        printf("n is ");
        n = get_int("Negative integer: ");
    }
    while (n > 0);
    return n;
}
