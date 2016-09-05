/**
 * David J. Malan
 * malan@harvard.edu
 *
 * Prints a string, one character per line.
 *
 * Demonstrates strings as arrays of chars and use of strlen.
 */

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // get line of text
    string s = get_string();

    // print string, one character per line
    for (int i = 0; i < strlen(s); i++)
    {
        printf("%c\n", s[i]);
    }
}
