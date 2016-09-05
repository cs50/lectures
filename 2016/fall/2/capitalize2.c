/**
 * David J. Malan
 * malan@harvard.edu
 *
 * Capitalizes a given string.
 *
 * Demonstrates further simplification of code with toupper.
 */

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // get line of text
    string s = get_string();

    // capitalize text
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", toupper(s[i]));
    }
    printf("\n");
}
