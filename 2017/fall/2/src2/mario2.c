// Prints any number of question marks, as specified by user

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_int("Number: ");
    for (int i = 0; i < n; i++)
    {
        printf("?");
    }
    printf("\n");
}
