#include <stdio.h>

int main()
{
    // Logarithmic Time -> O(nlog n)

    
    int n = 5;
    for (int i = 1; i <= n; i++) {
        int j = i;
        while (j > 0) {
            printf("i = %d, j = %d\n", i , j);
            j = j / 2;
        }
    }
    
    return 0;
}