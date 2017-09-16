// Recursive binary search

#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Names in a phone book
string book[] = {
    "Chen",
    "Kernighan",
    "Leitner",
    "Lewis",
    "Malan",
    "Muller",
    "Seltzer",
    "Shieber",
    "Smith"
};

int main(void)
{
    // Prompt user for name
    string name = get_string("Name: ");

    // Search for name
    int left = 0, right = sizeof(book) / sizeof(string) - 1;
    while (left <= right)
    {
        // Look at middle
        int middle = (left + right) / 2;
        if (strcmp(name, book[middle]) == 0)
        {
            printf("Calling %s\n", name);
            return 0;
        }

        // Search left half
        else if (strcmp(name, book[middle]) < 0)
        {
            right = middle - 1;
        }

        // Search right half
        else if (strcmp(name, book[middle]) > 0)
        {
            left = middle + 1;
        }
    }
    printf("Quitting\n");
    return 1;
}
