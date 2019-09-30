// Compares two strings using strcmp and !

#include <cs50.h>
#include <stdio.h>
#include <string.h>

bool string_compare(string a, string b);

int main(void)
{
    // Get two strings
    string s = get_string("s: ");
    string t = get_string("t: ");

    // Compare strings
    if (!strcmp(s, t))
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}

bool string_compare(string a, string b)
{
    // If different lengths
    if (strlen(a) != strlen(b))
    {
        return false;
    }

    // If different characters
    for (int i = 0, n = strlen(a); i < n; i++)
    {
        if (a[i] != b[i])
        {
            return false;
        }
    }

    // Same
    return true;
}
