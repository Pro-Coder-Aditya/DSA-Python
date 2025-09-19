#include <stdio.h>

int main()
{
    // Logarithmic Time -> O(log n)

    int n = 64;
    while (n > 0) {
        printf("%d\n", n);
        n = n / 2;
    }

    return 0;
}