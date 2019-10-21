// get_string and printf with %s

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("What's your name?\n");
    printf("hello, %s\n", s);
}
