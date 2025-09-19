#include <stdio.h>

int main()
{
    // Find the Time Complexity

    int n = 4;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("Pair: (%d, %d)\n", i, j);
        }
    }
    for (int k = 0; k < n; k++) {
        printf("Single: %d\n", k);
    }

    return 0;
}