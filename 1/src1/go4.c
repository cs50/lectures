// 1, 2, 3, go, 0-indexed

#include <stdio.h>

int main(void)
{
    int i = 0;
    while (i < 3)
    {
        printf("%i\n", i + 1);
        i++;
    }
    printf("go\n");
}
