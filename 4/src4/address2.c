// Prints an integer's address

#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%i\n", *&n);
}
