// Prompts user again if need be. (Poor design.)

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_int("What's n? ");
    if (n < 0)
    {
        n = get_int("What's n? ");
    }

    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
