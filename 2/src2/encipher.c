// Enciphers text

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string plaintext = get_string("Plaintext:  ");
    printf("Ciphertext: ");
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        printf("%c", plaintext[i] + 1);
    }
    printf("\n");
}
