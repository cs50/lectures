#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = 1;
    for (int i = 0; i < 64; i++)
    {
        printf("%i\n", n);
        n = n * 2;
    }
}
