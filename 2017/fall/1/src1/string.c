// get_string and printf with %s

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("name: ");
    printf("hello, %s\n", s);
}
