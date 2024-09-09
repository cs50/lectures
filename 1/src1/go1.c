// 1, 2, 3, go, with a loop

#include <stdio.h>

int main(void)
{
    int i = 1;
    while (i <= 3)
    {
        printf("%i\n", i);
        i = i + 1;
    }
    printf("go\n");
}
