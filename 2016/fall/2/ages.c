/**
 * David J. Malan
 * malan@harvard.edu
 *
 * Ages people by a year.
 *
 * Demonstrates arrays.
 */

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // determine number of people
    int n;
    do
    {
        printf("Number of people in room: ");
        n = get_int();
    }
    while (n < 1);

    // declare array in which to store everyone's age
    int ages[n];

    // get everyone's age
    for (int i = 0; i < n; i++)
    {
        printf("Age of person #%i: ", i + 1);
        ages[i] = get_int();
    }

    // report everyone's age a year hence
    printf("Time passes...\n");
    for (int i = 0; i < n; i++)
    {
        printf("A year from now, person #%i will be %i years old.\n", i + 1, ages[i] + 1);
    }
}
