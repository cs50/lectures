// Capitalizes a string

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // get a string
    string s = get_string("s: ");

    // copy string's address
    string t = s;

    // capitalize first letter in string
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    // print string twice
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}
