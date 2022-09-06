// Prints an n-by-n grid of bricks using three functions

#include <cs50.h>
#include <stdio.h>

int get_size(void);
void print_bricks(int n);
void print_row(int n);

int main(void)
{
    int n = get_size();
    print_bricks(n);
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

void print_bricks(int n)
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
