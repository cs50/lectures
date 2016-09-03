#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int c = get_char();
    switch (c)
    {
        case 'Y':
        case 'y':
            printf("yes\n");
            break;
        case 'N':
        case 'n':
            printf("no\n");
            break;
        default:
            printf("error\n");
            break;
    }
}
