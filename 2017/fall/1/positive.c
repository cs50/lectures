#include <cs50.h>
#include <stdio.h>

int get_positive_int();

int main(void)
{
    int i = get_positive_int();
    printf("%i is a positive integer\n", i);
}

int get_positive_int(void)
{
    int n;
    do
    {
        printf("n is ");
        n = get_int();
    }
    while (n < 1);
    return n;
}
