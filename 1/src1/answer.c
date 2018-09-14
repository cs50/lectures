// Logical operators

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for answer
    char c = get_char("Answer: ");

    // Check answer
    if (c == 'Y' || c == 'y')
    {
        printf("yes\n");
    }
    else if (c == 'N' || c == 'n')
    {
        printf("no\n");
    }
}
