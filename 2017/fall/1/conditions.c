#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int i = get_int();
    if (i < 0)
    {
        printf("negative\n");
    }
    else if (i > 0)
    {
        printf("positive\n");
    }
    else
    {
        printf("zero\n");
    }
}
