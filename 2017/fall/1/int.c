// Demonstrates get_int as well as printf with format string.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int i = get_int("integer: ");
    printf("hello, %i\n", i);
}
