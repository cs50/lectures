/**
 * David J. Malan
 * malan@harvard.edu
 *
 * Prints command-line arguments, one per line.
 *
 * Demonstrates use of argv.
 */

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    // print arguments
    for (int i = 0; i < argc; i++)
    {
        printf("%s\n", argv[i]);
    }
}
