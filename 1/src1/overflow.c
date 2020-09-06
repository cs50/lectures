// Integer overflow

#include <stdbool.h>
#include <stdio.h>
#include <unistd.h>

int main(void)
{
    // Iteratively double i
    int i = 1;
    while (true)
    {
        printf("%i\n", i);
        sleep(1);
        i *= 2;
    }
}
