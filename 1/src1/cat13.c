// Demonstrates scope

#include <stdio.h>

void meow(int n);

int main(void)
{
    int n = 3;
    meow(n);
}

// Meow some number of times
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
