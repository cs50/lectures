// Implements linear search for numbers

#include <stdio.h>

int main(void)
{
    // An array of numbers
    int numbers[] = {20, 500, 10, 5, 100, 1, 50};

    // Search for 50
    for (int i = 0; i < 7; i++)
    {
        if (numbers[i] == 50)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
