#include <stdio.h>

const unsigned int N = 3;

int main(void)
{
    int list[N];

    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    for (int i = 0; i < N; i++)
    {
        printf("%i\n", list[i]);
    }
}
