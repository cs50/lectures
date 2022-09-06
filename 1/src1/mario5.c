// Prints a column of n bricks using two functions

#include <cs50.h>
#include <stdio.h>

int get_height(void);
void print_bricks(int n);

int main(void)
{
    int n = get_height();
    print_bricks(n);
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

void print_bricks(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("#\n");
    }
}
