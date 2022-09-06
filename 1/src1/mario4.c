// Prints a column of n bricks using a function

#include <cs50.h>
#include <stdio.h>

int get_size(void);

int main(void)
{
    int n = get_size();
    for (int i = 0; i < n; i++)
    {
        printf("#\n");
    }
}

int get_size(void)
{
    int size;
    do
    {
        size = get_int("Size: ");
    }
    while (size < 1);
    return size;
}
