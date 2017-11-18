// Compares two strings' addresses

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // get two strings
    string s = get_string("s: ");
    string t = get_string("t: ");

    // compare strings' addresses
    if (s == t)
    {
        printf("same\n");
    }
    else
    {
        printf("different\n");
    }
}
