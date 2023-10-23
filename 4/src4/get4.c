// Now frankly, Valgrind would be our friend here, and could help us detect this error.

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *s = malloc(4);
    char *t = malloc(4);

    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);

    printf("t: ");
    scanf("%s", t);
    printf("t: %s\n", t);
}
