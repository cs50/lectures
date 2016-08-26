#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int c = get_char();
    if (c == 'Y' || c == 'y')
    {
        printf("yes\n");
    }
    else if (c == 'N' || c == 'n')
    {
        printf("no\n");
    }
    else
    {
        printf("error\n");
    }
}
