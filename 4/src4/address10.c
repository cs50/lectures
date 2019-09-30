// Stores and prints a string's address

#include <stdio.h>

int main(void)
{
    char *s = "EMMA";
    printf("%c\n", *s);
    printf("%c\n", *(s+1));
    printf("%c\n", *(s+2));
    printf("%c\n", *(s+3));
}
