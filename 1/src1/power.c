// Math library

#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    double base = get_double("Base: ");
    double exponent = get_double("Exponent: ");
    printf("Output: %.0f\n", pow(base, exponent));
}
