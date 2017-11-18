// Prints a string's characters using pointer arithmetic

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // get a string
    char *s = get_string("string: ");
    if (!s)
    {
        return 1;
    }

    // print string, one character per line
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c\n", *(s + i));
    }
    return 0;
}
