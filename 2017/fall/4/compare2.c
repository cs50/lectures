// Compares two strings for equality while checking for errors

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // get a string
    char *s = get_string("s: ");
    if (s == NULL)
    {
        return 1;
    }

    // get another string
    char *t = get_string("t: ");
    if (t == NULL)
    {
        return 1;
    }

    // compare strings for equality
    if (strcmp(s, t) == 0)
    {
        printf("same\n");
    }
    else
    {
        printf("different\n");
    }
    return 0;
}
