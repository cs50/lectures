// Prints a 3-by-3 grid of bricks with a helper function

#include <stdio.h>

void print_row(void);

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        print_row();
    }
}

void print_row(void)
{
    for (int j = 0; j < 3; j++)
    {
        printf("#");
    }
    printf("\n");
}
