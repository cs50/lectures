// Libraries (e.g., rounding with 4.20)

#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    float amount = get_float("Dollar Amount: ");
    printf("%.10f\n", amount);
    int pennies = round(amount * 100);
    printf("Pennies: %i\n", pennies);
}
