#include <stdio.h>

// copied
void print_arr(int arr[], int arr_len)
{
	int i;

	for (i = 0; i < arr_len; i++)
		printf("%d ", arr[i]);
	printf("\n");
}

void m_sum(int n, int m, int num[], int index)
{
	int i;

	if (index == m) {
		if (n == 0) {
			print_arr(num, index);
		}
		return;
	}

	for (i = 1; i <= n; i++) {
		num[index] = i;
		m_sum(n - i, m, num, index + 1);
	}
}

#define MAXN 100

int main()
{
	int num[MAXN], n, m;

	printf("input n, m: ");
	scanf("%d %d", &n, &m);
	m_sum(n, m, num, 0);
	return 0;
}
