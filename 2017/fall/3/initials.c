// Extracts a user's initials

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char initials[4];
    string s = get_string("Name: ");
    int length = 0;
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (isupper(s[i]))
        {
            initials[length] = s[i];
            length++;
        }
    }
    initials[length] = '\0';
    printf("%s\n", initials);
}
