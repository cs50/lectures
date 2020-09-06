#include <cs50.h>
#include <stdio.h>

int get_negative_int();

int main(void)
{
    int i = get_negative_int();
    printf("%i is a negative integer\n", i);
}

int get_negative_int(void)
{
    int n;
    do
    {
        printf("n is ");
        n = get_int();
    }
    while (n > 0);
    return n;
}
