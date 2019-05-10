#include <stdio.h>
//#include <inttype.h>

long long choose(int n, int r)
{
    if (r == 0 || n == r)
        return 1;
    return choose(n - 1, r - 1) + choose(n - 1, r);
}

#define MAXN 200

long long choose2(int n, int r)
{
    static long long memo[MAXN][MAXN];

    if (memo[n][r] > 0)
        return memo[n][r];

    if (r == 0 || n == r)
        return memo[n][r] = 1;
    else
        return memo[n][r] = choose2(n - 1, r - 1) + choose2(n - 1, r);
}

int main()
{
    int n, r;

    printf("input n, r: ");
    scanf("%d %d", &n, &r);
    printf("%lld\n", choose(n, r));
    return 0;
}
