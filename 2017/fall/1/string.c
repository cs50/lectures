// Demonstrates get_string as well as printf with format string.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("name: ");
    printf("hello, %s\n", s);
}
