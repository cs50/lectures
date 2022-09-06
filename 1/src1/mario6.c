// Prints a 3-by-3 grid of bricks with two helper functions

#include <cs50.h>
#include <stdio.h>

void print_rows(int n);
void print_row(int n);

int main(void)
{
    print_rows(3);
}

void print_rows(int n)
{
    for (int i = 0; i < n; i++)
    {
        print_row(n);
    }
}

void print_row(int n)
{
    for (int j = 0; j < n; j++)
    {
        printf("#");
    }
    printf("\n");
}
