// Linear search

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
    for (int i = 0; i < sizeof(book) / sizeof(string); i++)
    {
        if (strcmp(name, book[i]) == 0)
        {
            printf("Calling %s\n", name);
            return 0;
        }
    }
    printf("Quitting\n");
}
