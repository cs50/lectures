#include <stdio.h>
#include <stdlib.h>

int binarySearch(int array[], int size, int key) {
    int low = 0, high = size - 1, mid;

    while (low <= high) {
        mid = (low + high) / 2;

        if (array[mid] == key)
            return mid;
        else if (array[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

int main() {
    int array[100], n, key, result;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    printf("Enter %d integers in ascending order: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    printf("Enter the key to search: ");
    scanf("%d", &key);

    result = binarySearch(array, n, key);

    if (result == -1)
        printf("%d is not found in the array.\n", key);
    else
        printf("%d is found at index %d.\n", key, result);

    return 0;
}
