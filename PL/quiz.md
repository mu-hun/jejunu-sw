# PL

## 프로그래밍 언어 설계

### 효율성

- 언어 설계의 최적화 : 좋은 언어 설계는 번역기가 효율적인 실행 코드를 생성할 수 있도록 돕는다.
- 번역의 효율성 : 원시 코드가 효율적으로 번역되도록 허가하는지, 즉 알맞은 크기의 번역기로 빠르게(컴파일러 측) 번역할 수 있는가?

- 딘일 패스 컴파일러 구성
  - Algol 68 : 허상 참조 방지

### 일반성

밀칩하게 관련이 있는 여러 개념들을 일반적인 하니의 개념으로 결함히여 일반성(generality)을 취득한다.

예) 값 전달 기법과 객체에 대한 참조 기능 지원

이율 배반성 : 다만 다른 원칙을 거스르는 위험성이 있다. 언어를 모호하게 만들거나 신뢰성을 낮춘다.

예) C의 포인터는 신뢰성과 판독성을 낮춘다. 보상으로 매우 큰 일반성을 제공한다.

### 획일성

언어 구조들의 외모와 행동에서의 조화에 중점을 둔다.

비조화는 두 가지 형태를 가지고 있다.

- 유시한 것들이 유시하게 보이지 않거나 서로 다르게 행동하는 것이고,

- 유사하지 않은 것들이 의도되지 않았는데도 불구하고 유시하게 보이거니 유시하게 행동하는 것이다.

### 퀴즈

1. 지난 40 년 동안 프로그래밍 언어 설계에 가장 강력하게 영향을 미친 설계 기준은 무엇인가?

2. 프로그램의 주석에 대한 상반된 주장이 다음과 같다.

   (1) 프로그램은 밀기 쉽고 유지 보수하기 쉽도록 주석을 항상 포함해야 한다

   (2) 프로그램은 가능하면 자체 문서화 되어야 하며 주석은 코드 부분이 명확하게 이 해되지 않는 부분에만 최소한으로 사용되어야 한다.

언어 설계 측면에서 이 두 가지 관점에 대해 토론해 보아라.

> 여기서 추상화란 프로그래밍 언어로서의 추상화로, 자연어에 가까울수록 높다.

언어의 추상화 정도가 높다면 자체 문서화 될 조건에 성랍할 수 있다. 따라서 (2)의 조건으로 충분하다.

하지만 기계와 밀접한 수준의 낮은 추상화를 제공하는 언어의 경우 유지 보수를 위해 주석으로 추가적 설명이 필요하다.

## 프로그래밍 언어의 구문과 구현 기법

### 프로그래밍 언어가 갖는 예약어에 대하여 설명하고 단점을 설명하라

### 다음은 Algol 이 60 에 정의된 for 문장에 관한 BNF이다

```bnf
<for stmt> ::= <for clause><strmt> | <label> : <for stmt>
<for clause> ::= for <variable> := <for list> do
<for list> := <for list element> | <for list>, <for list element>
<for list element> ::= <arithmetic expr> |
    <arithmetic expr> step <arithmetic exep>
    until <arithmetic expr> | 
    <arithmetic exep> while
    <boolean exp>
```

1. 위 BNF를 EBNF로 표현하라

   ```ebnf
   <for stmt> ::= [<label> :] {<for clause><strmt>}
   <for clause> ::= for <variable> := <for list element> do
   <for list element> ::= {<arithmetic expr> |
       <arithmetic expr> step <arithmetic exep>
       until <arithmetic expr> |
       <arithmetic exep> while
       <boolean exp>}
   ```

2. 위 BNF를 구문 도표로 표현하라

### 바인딩
