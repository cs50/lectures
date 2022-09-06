// Prints a column of n bricks using a function

#include <cs50.h>
#include <stdio.h>

int get_height(void);

int main(void)
{
    int n = get_height();
    for (int i = 0; i < n; i++)
    {
        printf("#\n");
    }
}

int get_height(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1);
    return height;
}
