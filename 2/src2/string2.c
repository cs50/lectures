// Prints string all at once using printf, which figures out its length

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("Input:  ");
    printf("Output: %s\n", s);
}
