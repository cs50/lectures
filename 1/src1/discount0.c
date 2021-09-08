// Return value

#include <cs50.h>
#include <stdio.h>

float discount(float price);

int main(void)
{
    float regular = get_float("Regular Price: ");
    printf("Sale Price: %.2f\n", discount(regular));
}

// Discount price
float discount(float price)
{
    return price * .85;
}
