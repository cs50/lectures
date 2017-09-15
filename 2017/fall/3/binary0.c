// Iterative binary search

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

bool search(string name, string names[], int left, int right);

int main(void)
{
    // Prompt user for name
    string name = get_string("Name: ");

    // Search for name
    if (search(name, book, 0, sizeof(book) / sizeof(string) - 1))
    {
        printf("Calling %s\n", name);
    }
    else
    {
        printf("Quitting\n");
    }
}

// Searches names for name
bool search(string name, string names[], int left, int right)
{
    // No more names to search
    if (left > right)
    {
        return false;
    }

    // Look at middle
    int middle = (left + right) / 2;
    if (strcmp(name, names[middle]) == 0)
    {
        return true;       
    }

    // Search left half
    else if (strcmp(name, names[middle]) < 0)
    {
        return search(name, names, left, middle - 1);
    }

    // Search right half
    else if (strcmp(name, names[middle]) > 0)
    {
        return search(name, names, middle + 1, right);
    }

    return false;
}
