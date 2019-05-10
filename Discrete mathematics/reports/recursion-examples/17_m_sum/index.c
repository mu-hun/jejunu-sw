#include <stdio.h>

#define MAXN 100
#define min(x, y) ((x)<(y)?(x):(y))

void m_sum(int n, int m, int num[], int l, int t)
{
    int i;

    if (l == m) {
        if (n != 0)
            return;
        for (i = 0; i < l; i++)
            printf("%d ", num[i]);
        printf("\n");
        return;
    }

    for (i = 0; i <= min(t, n); i++) {
        num[l] = i;
        m_sum(n - i, m, num, l + 1, i);
    }
}

int main()
{
    int num[MAXN], n, m;

    printf("input n, m: ");
    scanf("%d %d", &n, &m);
    m_sum(n, m, num, 0, n);
    return 0;
}
