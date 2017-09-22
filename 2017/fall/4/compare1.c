// Compares two strings for equality

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // get two strings
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    // compare strings for equality
    if (strcmp(s, t) == 0)
    {
        printf("same\n");
    }
    else
    {
        printf("different\n");
    }
}
