#include <stdio.h>

int main()
{
    // Cubic Time -> O(n^3)

    int n = 4;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= n; k++) {
                printf("Group: %d, %d, %d\n", i, j, k);
            }
        }
    }

    return 0;
}