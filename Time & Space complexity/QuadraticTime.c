#include <stdio.h>

int main()
{
    // Quadratic Time -> O(n^2)

    int n = 5;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            printf("Team: Num %d with Num %d\n", i, j);
        }
    }

    return 0;
}