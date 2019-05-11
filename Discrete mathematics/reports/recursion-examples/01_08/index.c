//
// Created by Muhun Kim on 2019-05-08.
//

#include <stdio.h>
#define N 100

const int int_size = sizeof(int);
const int NIL = -1;
int fib_lookup_table[N];
int factor_lookup_table[N];


void memo_initials()
{
    for(int i=0; i<N; i++) {
        fib_lookup_table[i] = NIL;
        factor_lookup_table[i] = NIL;
    }
}

int startProject(int m) {
    printf("[startProject] motivation: %d\n", ++m);
    return m;
}
int loseMotivation(int m) {
    printf("[loseMotivation] motivation: %d\n", --m);
    return m;
}
int abandonProject(int m) {
    printf("[abandonProject] motivation: %d\n", --m);
    return m;
}
void haveGreatIdea(int m, int acc, int callStack) {

    if (acc++ > callStack) {
        printf("\nlimit motivation: %d\n", m);return;
    }

    printf("\nOn I have a great idea!\n");

    haveGreatIdea(
            abandonProject(
                    loseMotivation(
                            startProject(m))), acc, callStack);
}


void startProjectP(int *m) {
    printf("[startProject] motivation: %d\n",  *m+=1);
}
void loseMotivationP(int *m) {
    printf("[loseMotivation] motivation: %d\n",  *m-=1);
}
void abandonProjectP(int *m) {
    printf("[abandonProject] motivation: %d\n",  *m-=1);
}
void haveGreatIdeaP(int *m, int callStack) {
    if (callStack++ > 10) {
        printf("[haveGreatIdea] last motivation: %d\n", *m);return;
    }
    startProjectP(m);
    loseMotivationP(m);
    abandonProjectP(m);
    haveGreatIdeaP(m, callStack);
}


int fibonacci(int n) {
    if (n == 1 || n == 2)
        return 1;
    else
        return fibonacci(n-1) + fibonacci(n-2);
}


int fib_memo(int n) {
    if(fib_lookup_table[n] == NIL) {
        if(n <= 1)
            fib_lookup_table[n] = n;
        else
            fib_lookup_table[n] = fib_memo(n-1) + fib_memo(n-2);
    }
    return fib_lookup_table[n];
}

int factorial(int n) {
    if (n==0) return 1;
    return n * factorial(n - 1);
}


int factorial_memo(int n) {
    if (factor_lookup_table[n] == NIL) {
        if (n <= 1)
            factor_lookup_table[n] = n;
        else
            factor_lookup_table[n] = n * factorial_memo(n-1);
    }
    return factor_lookup_table[n];
}

int _factorial_tail(int n, int acc) {
    return (n <= 1? acc : _factorial_tail(n-1, n*acc));
}

int factorial_tail(int n) {
    return _factorial_tail(n, 1);
}

int main(void) {
    int x, y;

    memo_initials();

    printf("crunch values: ");
    scanf("%d %d", &x, &y);

	haveGreatIdea(x, 0, y);

//    printf("\n\nhaveGreatIdea: motivation by pointer:\n");
//    haveGreatIdeaP(&x, 0);

    printf("fibonacci(3) is 1 : %s\n", fibonacci(3) == 2 ? "true" : "false");
    printf("fib_memo(3) is 1 : %s\n", fib_memo(3) == 2 ? "true" : "false");
    printf("factorial(3) : %s\n", factorial(3) == 6 ? "true" : "false");
    printf("factorial_memo(3) is 1 : %s\n", factorial_memo(3) == 6 ? "true" : "false");
    printf("factorial_tail(3) is 1 : %s\n", factorial_tail(3) == 6 ? "true" : "false");

    return 0;

}
