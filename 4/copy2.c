#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    printf("s: ");
    char *s = get_string();
    if (s == NULL)
    {
        return 1;
    }

    char *t = malloc((strlen(s) + 1) * sizeof(char));
    if (t == NULL)
    {
        return 1;
    }

    for (int i = 0, n = strlen(s); i <= n; i++)
    {
        *(t + i) = *(s + i);
    }

    if (strlen(t) > 0)
    {
        *t = toupper(*t);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);

    return 0;
}
