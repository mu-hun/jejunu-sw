# 빅-오 계산하기

## 어느 알고리즘이 두 단계로 수행되는데, 1단계는 O(N) 시간이 걸리고 2단계에는 O(N^2)이 소요된다. 이 알고리즘의 총 수행시간을 표현하시오

O(N^2)

> N이 매우 큰 경우에는 실행횟수(시간)은 차수가 높은 항에 크게 영향을 받게 된다.

> O-표기법은 말 그대로 점근표기법이기 때문에 N가 매우 큰 경우를 가정하는 것임

## 빅-오 표기법의 실행 시간이 큰 순서

`N! > 2^N N^3 > N^2 > 5N logN N logN^3 > N loglogN > 3N > N^1/2 > 100`

## 다음 파이썬 코드의 실행 시간을 표현하시오

### 이중 루프 I

```python
s = 0
for i in range(N):
    for j in range(N):
        s += N
```

![five](../images/five.svg)

### 이중 루프 II

```python
s = 0
for i in range(N):
    for j in range(i):
        s += j
```

O(N^2)

### 삼중 루프

```python
r = 0
for i in range(N):
    for j in range(i+1, N+1):
        for k in range(j+1):
            r += 1
```

O(N^3)
