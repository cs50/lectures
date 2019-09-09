// get_float and printf with %f

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int price = get_float("What's the price?\n$");
    printf("Your total is $%.2f.\n", price * 1.0625);
}
