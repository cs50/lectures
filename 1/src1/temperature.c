// Floating-point arithmetic

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float f = get_float("F: ");
    float c = 5.0 / 9.0 * (f - 32.0);
    printf("C: %.1f\n", c);
}
