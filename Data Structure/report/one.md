# 빅-오 계산하기

## 어느 알고리즘이 두 단계로 수행되는데, 2단계는 O(N) 시간이 걸리고 2단계에는 O(N^2)이 소요된다. 이 알고리즘의 총 수행시간을 표현하시오

![one](../images/one.svg)

## 실행 시간이 큰 순서

![two](../images/two.svg)

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

![three](../images/three.svg)

### 삼중 루프

```python
r = 0
for i in range(N):
    for j in range(i+1, N+1):
        for k in range(j+1):
            r += 1
```

![four](../images/four.svg)

