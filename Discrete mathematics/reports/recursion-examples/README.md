# 재귀함수 30개

|  이름  |    학번    |         개발 환경          |
| :----: | :--------: | :------------------------: |
| 김무훈 | 2018103277 | cmake 3.13, Clion 2018.3.0 |

## 폴더 구조

```bash
❯ ls 01_08
CMakeLists.txt index.c
```

폴더 이름을 `09_구현명` 혹은 `10_12_구현명` 같이 오름차순으로 지정했습니다.

다만 여러 구현체가 모아진 `01_08`는 `구현명`을 붙지 않았습니다.

각 폴더의 `index.c` 에는 실제로 가능한 구현체의 소스가 들어있으며, 입출력 예를 `main()` 함수 내에 준비하였습니다.

## 출처

|      범위     |  원본 혹은 하위링크  |
| :------: | :----------: |
|                      `09_pay`부터 `19_21_linked_list`                      |                   "문제로 풀어보는 알고리즘" 황인욱, 김용혁 - 01 재귀적 프로그래밍 (41~74 쪽)                    |
| `22_mergesort`, `23_quicsort`, `24_tower_of_hanoi` `25_27_tree_traversals` | G[1]`merge-sort`, `quick-sort`, `c-program-for-tower-of-hanoi`, `tree-traversals-inorder-preorder-and-postorder` |
|                              `29_palindrome`                               |          C Program to Check whether a given String is Palindrome or not using Recursion - Sanfoundry[2]          |

> 1: https://www.geeksforgeeks.org/<하위링크>
>
> \*`merge-sort`의 경우 `https://www.geeksforgeeks.org/merge-sort/`를 가리킵니다.
>
> 2: https://www.sanfoundry.com/c-program-string-palindrome-using-recursion/

[1]: https://www.geeksforgeeks.org/
[2]: https://www.sanfoundry.com/c-program-string-palindrome-using-recursion/

위의 표에 명시하지 않은 `01_08`, `21_binary_search`, `28_percentage`, `30_print_array`는 직접 작성했습니다.

## 프로젝트 번복으로 과로에 지친 프로그래머

```c
crunch values: 10 10

On I have a great idea!
[startProject] motivation: 11
[loseMotivation] motivation: 10
[abandonProject] motivation: 9
...
On I have a great idea!
[startProject] motivation: 1
[loseMotivation] motivation: 0
[abandonProject] motivation: -1

limit motivation: -1
```

|  폴더   | 라인  | 함수 이름                                                                                    |  추가 구현  |
| :-----: | :---: | ------- | :-------: |
| `01_08` | 22~66 | `haveGreatIdea(int m, int acc, int callStack)`, <br> `haveGreatIdeaP(int *m, int callStack)` | 포인터 사용 |

프로그래머의 체력과 프로젝트 번복 주기를 입력한다. 포인터 구현체의 경우 번복 주기가 10으로 고정되어 있습니다.

## 피보나치 수

```c
// fibonacci(3) == 2 ? "true" : "false"
fibonacci(3) is 1 : true
fib_memo(3) is 1 : true
```

|  위치   | 라인  | 함수 이름                                |  추가 구현   |
| :-----: | :---: | ---------------------------------------- | :----------: |
| `01_08` | 69~85 | `fibonacci(int n)`,<br>`fib_memo(int n)` | 메모이제이션 |

캐싱할 N개의 배열을 `fibo_memo_initial()`로 초기화하고 `fib_mem(int n)`로 실행하면 된다.

## 팩토리얼

```c
factorial(3) : true
factorial_memo(3) is 1 : true
factorial_tail(3) is 1 : true
```

|  위치   |  라인  | 함수 이름                                                                        | 추가 구현 |
| :-----: | :----: | -------------------------------------------------------------------------------- | :-------: |
| `01_08` | 93~109 | `factorial(int n)`,<br>`factorial_memo(int n)`,<br>`_factorial_tail(int n, acc)` | 꼬리 재귀 |

## 금액 맞추기

```c
input number of bills: 6	// 여섯 종류의 지폐가 있음을 입력
input bills: 1 2 5 10 20 50	// 지페의 종류를 입력
input money: 100		// 100만원을 지불해야 함을 입력
4562
```

|   위치   | 함수 이름                            |
| :------: | ------------------------------------ |
| `09_pay` | `pay(int money, int bills[], int n)` |

## 수분할

```c
input n, m: 5 3
5
1 1 1 1 1
2 1 1 1
2 2 1
3 1 1
3 2
total 5
```

|       위치        | 함수 이름                                                                                                                                      |   추가 구현    |
| :---------------: | ---------------------------------------------------------------------------------------------------------------------------------------------- | :------------: |
| `10_12_partition` | `partition(int n, int m)`,<br>`partition_print(int n, int m, int arr[], int arr_len)`<br>`partition_memo(int n, int m)`<br>`partition2(int n)` | 분할의 가짓 수 |

`n`과 `m`을 입력받아서 정수 `n` 을 `m` 이하의 수로 분할하는 방법과 가짓 수를 출력한다.

## 수분할 2

```c
input n: 10
input length: 4
1
2
3
4
10
```

|         위치         | 함수 이름                                                                   |
| :------------------: | --------------------------------------------------------------------------- |
| `13_partition_count` | `partition_memo(int n, int m)`,<br>`partition_count(int n, int a[], int l)` |

m 가지의 수로 n을 분할하는 방법을 알려준다.

## 그레이 코드

```c
4
0000
0001
0011
0010
0110
0111
0101
0100
1100
1101
1111
1110
1010
1011
1001
1000
```

|  위치   | 함수 이름                                                                                                                                                     |                 비고                 |
| :-----: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------: |
| `14-16` | `print_gray(int code[], int n, int index)`,<br>`print_gray_reverse(int code[], int n, int index)`<br>`print_gray2(int code[], int n, int index, int reverse)` | 상호의존적으로<br>모든 함수를 설계함 |

그래이 코드란 연속된 수를 한 비트만 다르게 인코딩하는 방법이다.

연속적으로 변하는 양을 나타내고자 할때 변화폭이 적어 오류를 줄일 수 있어 데이터 전송에서 많이 쓰인다.

## 수분할 3

```
input n, m: 5 3
1 1 3
1 2 2
1 3 1
2 1 2
2 2 1
3 1 1
```

|    위치    | 함수 이름                                   |
| :--------: | ------------------------------------------- |
| `17_m_sum` | `m_sum(int n, int m, int num[], int index)` |

n과 m을 입력받아서(n>=m), m개의 자연수를 더해서 n을 만드는 모든 방법을 출력한다.

## 이항계수

```c
input n, r: 30 10
3004515
```

|    위치     | 함수 이름                                                             |            추가 구현             |
| :---------: | --------------------------------------------------------------------- | :------------------------------: |
| `18_choose` | `long long choose(int n, int r)`<br>`long long choose2(int n, int r)` | `choose2` 는 메모이제이션 구현체 |

n개의 원소를 가지는 집합에서 크기가 r인 부분집합을 고르는 경우의 수를 이항계수라고 하며 `nCr`로 나타낸댜.

n과 r을 입력받아 그 경우를 출력하는 함수이다.

## 연결 리스트 출력

```c
input number: 1
input number: 2
input number: 3
input number: 4
input number: -1
1 2 3 4 //print_list*
```

|        위치         | 함수 이름                                                     |         추가 구현          |
| :-----------------: | ------------------------------------------------------------- | :------------------------: |
| `19_20_linked_list` | `print_list2(node_t * from)`<br>`print_list_r(node_t * from)` | `print_list_r`는 역순 출력 |

## 이진탐색

```c
input codes:
int arr[] = { 2, 3, 4, 10, 40 };
int n = sizeof(arr) / sizeof(arr[0]);
int x = 10;
int result = binarySearch(arr, 0, n - 1, x);

output:
Element is present at index 2
```

|        위치        | 함수 이름                                       |
| :----------------: | ----------------------------------------------- |
| `21_binary_search` | `binary_search(int arr[], int L, int R, int x)` |

## 병합정렬

```
Given array is
12 11 13 5 6 7

Sorted array is
5 6 7 11 12 13
```

|      위치       | 함수 이름                            |
| :-------------: | ------------------------------------ |
| `22_merge_sort` | `mergeSort(int arr[], int l, int r)` |

## 퀵정렬

```
Sorted array: n1 5 7 8 9 10 n
```

|      위치      | 함수 이름                                 |
| :------------: | ----------------------------------------- |
| `23_quicksort` | `quickSort(int arr[], int low, int high)` |

## 하노이 탑

```
 Move disk 1 from rod A to rod B
 Move disk 2 from rod A to rod C
 Move disk 1 from rod B to rod C
 Move disk 3 from rod A to rod B
 Move disk 1 from rod C to rod A
 Move disk 2 from rod C to rod B
 Move disk 1 from rod A to rod B
 Move disk 4 from rod A to rod C
 Move disk 1 from rod B to rod C
 Move disk 2 from rod B to rod A
 Move disk 1 from rod C to rod A
 Move disk 3 from rod B to rod C
 Move disk 1 from rod A to rod B
 Move disk 2 from rod A to rod C
 Move disk 1 from rod B to rod C
```

|        위치         | 함수 이름                                                       |
| :-----------------: | --------------------------------------------------------------- |
| `24_tower_of_hanoi` | `towerOfHanoi(int n, char from_rod, char to_rod, char aux_rod)` |

## 트리 순회

```c
Preorder traversal of binary tree is
1 2 4 5 3
Inorder traversal of binary tree is
4 2 5 1 3
Postorder traversal of binary tree is
4 5 2 3 1
```

|          위치           | 함수 이름                                                                                                      |
| :---------------------: | -------------------------------------------------------------------------------------------------------------- |
| `25_27_tree_traversals` | `printPostorder(struct node* node)`<br>`printInorder(struct node* node)`<br>`printPreorder(struct node* node)` |

## 어떤 수의 백분율

```
Enter a value to split in percentage: 50

  1 Percent = 0.50
  2 Percent = 1.00
  3 Percent = 1.50
  4 Percent = 2.00
  5 Percent = 2.50
 ...
 96 Percent = 48.00
 97 Percent = 48.50
 98 Percent = 49.00
 99 Percent = 49.50
100 Percent = 50.00
```

|      위치       | 함수                       |
| :-------------: | -------------------------- |
| `28_percentage` | `RecursvFcnTogetPrcntge()` |

## 펠린드롬(앞뒤로 같은 문자)

```
Enter a word to check if it is a palindrome
asdffdsa
The entered word is a palindrome
```

|      위치       | 함수                            |
| :-------------: | ------------------------------- |
| `29_palindrome` | `check(char word[], int index)` |

## 배열 출력

```
4 12 9 34 6 8
```

|       위치       | 함수                           |
| :--------------: | ------------------------------ |
| `30_print_array` | `print_array(int arr[],int n)` |
