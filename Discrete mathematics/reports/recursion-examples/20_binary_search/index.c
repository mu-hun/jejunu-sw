#include <stdio.h>

int binary_search(int arr[], int L, int R, int x) {
    if(L <= R) {
        int mid = (L + R)/2;  /*low + (high - low)/2;*/

        if((mid == 0 || x > arr[mid-1]) && (arr[mid] == x))
            return mid;
        if(x > arr[mid])
            return binary_search(arr, (mid + 1), R, x);
        return binary_search(arr, L, (mid -1), x);
    }
    return -1;
}

int main(void)
{
    int arr[] = { 2, 3, 4, 10, 40 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int result = binary_search(arr, 0, n - 1, x);
    (result == -1) ? printf("Element is not present in array")
                   : printf("Element is present at index %d",
                            result);
    return 0;
}