#include <unistd.h>
#include <stdio.h>

int main()
{
    printf("alice:%s\n", crypt("apple", ".."));
    printf("bob:%s\n", crypt("banana", ".."));
    printf("carol:%s\n", crypt("cherry", ".."));
    printf("charlie:%s\n", crypt("cherry", ".."));
    printf("\n");
    printf("carol:%s\n", crypt("cherry", "50"));
    printf("charlie:%s\n", crypt("cherry", "49"));
}
