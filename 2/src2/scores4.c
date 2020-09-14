// Averages three numbers using an array, a constant, and a helper function

#include <cs50.h>
#include <stdio.h>

// Prototype
float average(int length, int array[]);

// Constant
int N = 3;

int main(void)
{
    // Get scores
    int scores[N];
    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score: ");
    }

    // Print average
    printf("Average: %f\n", average(scores, N));
}

float average(int length, int array[])
{
    // Calculate average
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return sum / (float) length;
}

