// Compares two strings for equality

#include <cs50.h>
#include <stdio.h>
#include <string.h>

bool compare_strings(char *a, char *b);

int main(void)
{
    // Get two strings
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    // Compare strings for equality
    if (compare_strings(s, t))
    {
        printf("same\n");
    }
    else
    {
        printf("different\n");
    }
}

bool compare_strings(char *a, char *b)
{
    // Compare strings' lengths
    if (strlen(a) != strlen(b))
    {
        return false;
    }

    // Compare strings character by character
    for (int i = 0, n = strlen(a); i < n; i++)
    {
        // Different
        if (a[i] != b[i])
        {
            return false;
        }
    }

    // Same
    return true;
}
