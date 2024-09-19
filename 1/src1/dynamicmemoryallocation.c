#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, *arr, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    arr = (int*)malloc(n * sizeof(int));

    if (arr == NULL) {
        printf("Memory not allocated.\n");
        return 1;
    }

    printf("Enter %d integers: ", n);
    for (i = 0; i < n; i++) {
        scanf("%d", arr + i);
    }

    printf("Array elements are: ");
    for (i = 0; i < n; i++) {
        printf("%d ", *(arr + i));
    }
    printf("\n");

    free(arr);
    return 0;
}
