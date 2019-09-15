// Return value

#include <stdio.h>

void square(int n);

int main(void)
{
    int input = get_int("Input: ");
    printf("Output: %i\n", square(n));
}

// Square n
int square(int n)
{
    return n * n;
}
