#include <stdio.h>

int main()
{
    // Linear Time -> O(n)

    int arr[] = {1, 2, 3, 4, 5};
    int n = 5;
    for (int i = 0; i < n; i++) {
        printf("%d\n", arr[i]);
    }

    return 0;
}