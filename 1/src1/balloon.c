// Animation

#include <stdio.h>
#include <unistd.h>

int main(void)
{
    for (int i = 0; i < 50; i++)
    {
        printf("\n");
    }
    printf("🎈");
    for (int i = 0; i < 50; i++)
    {
        printf("\n");
        sleep(1);
    }
}
