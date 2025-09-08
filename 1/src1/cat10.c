// Uses a do-while loop instead.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("What's n? ");
    }
    while (n < 0);

    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
