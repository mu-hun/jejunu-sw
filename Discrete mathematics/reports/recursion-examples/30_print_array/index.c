#include<stdio.h>
void print_array(int arr[],int n)
{
    if(n<0) return;
    print_array(arr,n-1);
    printf("%d ",arr[n]);
}
int main()
{
    int arr[6]={4,12,9,34,6,8};
    print_array(arr,5);
    return 0;
}