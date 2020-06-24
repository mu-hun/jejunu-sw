# 정돈한 스키마 정보

## 테이블 이름

| chinese | 중국인 관광객 데이터 |
| :--: | :--: |
| local | 국내 관광객 데이터 |

## Chinese

| 속성 | 설명 |
| :--: | -- |
| `BillingAmount1`|  2014-2015년 카드 이용 금액 |
| `BillingCount1` | 2014-2015년 카드 이용 건수 |
| `BillingPeople1`|  2014-2015년 카드 이용 고객 수 |
| `BillingAmount2`|  2015-2016년 카드 이용 금액 |
| `BillingCount2` | 2015-2016년 카드 이용 건수 |
| `BillingPeople2`|  2015-2016년 카드 이용 고객 수 |

## local

| 속성 | 설명 |
| :--: | :--: |
| `BillingAmount` | 카드 이용 금액 |
| `BillingCount` | 카드 이용 건수 |
| `BillingPerCount` | 건당 이용 금액 |

---

## 2014~2016년 전용 `chinese` 속성 만들기

```sql
ALTER TABLE chinese
  ADD BillingAmount FLOAT NULL
ALTER TABLE chinese
  ADD BillingCount FLOAT NULL
ALTER TABLE chinese
  ADD BillingPeople FLOAT NULL
ALTER TABLE chinese
  ADD BillingPerCount FLOAT NULL`
```

미리 채울 테이블의 속성을 만들어 낸다.

| 속성 | 설명 |
| :--: | -- |
| `BillingAmount`|  카드 이용 금액 |
| `BillingCount1` | 카드 이용 건수 |
| `BillingPeople1`|  카드 이용 고객 수 |

## 위 속성의 데이터 채우기

```sql
UPDATE chinese
  SET BillingAmount = BillingAmount1 + BillingAmount2;
UPDATE chinese
  SET BillingPeople = BillingPeople1 + BillingPeople2;
UPDATE chinese
  SET BillingCount = BillingCount1 + BillingCount2
UPDATE chinese
  SET BillingPerCount = ROUND(BillingAmount / BillingPeople, 0)
```

## 가상 뷰 만들기

```sql
CREATE VIEW chineseView AS
  SELECT country,
    SUM(BillingAmount) AS 'CountryBillingAmount',
    SUM(BillingPeople) AS 'CountryBillingPeople',
    SUM(BillingPerCount) AS 'BillingPerCount'
  FROM chinese
  GROUP BY country

CREATE VIEW localView AS
  SELECT country,
    SUM(BillingAmount) AS 'CountryBillingAmount',
    SUM(BillingCount) AS 'CountryBillingCount',
    sum(BillingPerCount) AS 'BillingPerCount'
  FROM local
  GROUP BY country
```

중국인 관광객 데이터가 담긴 뷰를 chineseView 라는 이름으로 만들고, 내국인 관광객 데이터가 담긴 뷰를 localView 이름으로 만들어냅니다.

country는 읍면동을 가리키는 속성입니다.

한국인보다 중국인이 더 많은 지역을 검색하기 이전에 `GROUP BY country`로 읍면동을 기준으로 미리 묶어놓읍시다.

## 결과 뷰 생성

```sql
CREATE VIEW resultView AS
  SELECT chineseView.country AS '읍면동', chineseView.BillingPerCount AS '건당 이용 금액'
  FROM chineseView, localView
  WHERE chineseView.country = localView.country
  AND chineseView.BillingPerCount > localView.BillingPerCount
```

읍면동을 기준으로 두 뷰의 건당 이용 금액을 비교하고, 국내 관광객보다 큰 수치를 갖는 중국인의 결제 정보를 찾아 `resultView` 에 집어넣습니다.

## 결과

| 읍면동 | 건당 이용 금액 |
| :--: | :--: |
| 대륜동 | 53500432 |
