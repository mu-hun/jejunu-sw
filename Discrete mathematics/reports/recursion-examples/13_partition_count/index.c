#include <stdio.h>

#define MAXN 200

int partition_memo(int n, int m)
{
    static int memo[MAXN][MAXN];
    int count = 0, i;

    if (n < m)
        m = n;
    if (memo[n][m] > 0)
        return memo[n][m];
    if (n == 0)
        return memo[n][m] = 1;

    for (i = 1; i <= m; i++)
        count += partition_memo(n - i, i);
    return memo[n][m] = count;
}

int partition_count(int n, int a[], int l)
{
	int r = 0, i;

	if (n <= 0)
		return 0;

	for(i=1; i < a[0]; i++)
		r += partition_memo(n - i, i);

	r += partition_count(n - a[0], a+1, l-1);
	return r;
}

int main()
{
    int a[MAXN];
	int n, l;

	int i;
	printf("input n: ");
	scanf("%d", &n);
	printf("input length: ");
	scanf("%d", &l);
	for(i=0; i<l; i++) {
		scanf("%d", &a[i]);
	}
	printf("%d\n", partition_count(n, a, l) + 1);
    return 0;
}
