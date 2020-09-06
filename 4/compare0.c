#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("s: ");
    string s = get_string();
 
    printf("t: ");
    string t = get_string();
 
    if (s == t)
    {
        printf("same\n");
    }
    else
    {
        printf("different\n");
    }
}
