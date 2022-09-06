// Prints a 3-by-3 grid of bricks with a helper function that takes an argument

#include <stdio.h>

void print_row(int n);

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        print_row(3);
    }
}

void print_row(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
    printf("\n");
}
