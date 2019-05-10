#include <stdio.h>

int pay(int money, int bills[], int n)
{
    int count = 0, i, t;

    if (n == 1) {
        if (money % bills[0] == 0)
            return 1;
        else
            return 0;
    }

    t = money / bills[n - 1];
    for (i = 0; i <= t; i++)
        count += pay(money - bills[n - 1] * i, bills, n - 1);
    return count;
}

#define MAXN 50

int main()
{
    int num_bills, money, i;
    int bills[MAXN];

    printf("input number of bills: ");
    scanf("%d", &num_bills);
    printf("input bills: ");
    for (i = 0; i < num_bills; i++)
        scanf("%d", &bills[i]);
    printf("input money: ");
    scanf("%d", &money);
    printf("%d\n", pay(money, bills, num_bills));
    return 0;
}
