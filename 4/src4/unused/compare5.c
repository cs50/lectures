// Compares two strings using strcmp and !

#include <cs50.h>
#include <stdio.h>
#include <string.h>

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
