/*
 * Demonstrates a better name for a variable.
 */

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string();
    printf("hello, %s\n", name);
}
