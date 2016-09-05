/**
 * David J. Malan
 * malan@harvard.edu
 *
 * Prints a string, one character per line.
 *
 * Demonstrates error checking.
 */

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // get line of text
    string s = get_string();

    // print string, one character per line
    if (s != NULL)
    {
        for (int i = 0; i < strlen(s); i++)
        {
            printf("%c\n", s[i]);
        }
    }
}
