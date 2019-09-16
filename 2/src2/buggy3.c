// Buggy example for help50, debug50

#include <cs50.h>
#include <stdio.h>

int get_negative_int(void);

int main(void)
{
    int i = get_negative_int();
    printf("%i\n", i);
}

// Prompt user for positive integer
int get_negative_int(void)
{
    do
    {
        int n = get_int("Negative Integer: ");
    }
    while (n < 0);
    return n;
}
