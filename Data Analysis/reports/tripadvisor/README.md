# 트립어드바이저 리뷰 수집 및 시각화하기

[트립어드바이저](https://www.tripadvisor.co.kr)는 관광 리뷰를 게시하거나 볼 수 있는 서비스입니다. 리뷰 수집 및 단어빈도분석을 하는 파이썬 프로그램을 작성하세요.

1. [한라산국립공원 리뷰](https://www.tripadvisor.co.kr/Attraction_Review-g297892-d550726-Reviews-Hallasan_National_Park-Seogwipo_Jeju_Island.html)를 수집 후 CSV로 정규화하기
2. 형태소 분석으로 단어를 추출하고 빈도가 높은 상위 20개 단어 목록을 막대 그래프로 출력하기

## 필요한 외부 파이썬 모듈

- requests
- pandas
- matplotlib
- [konlpy](https://konlpy-ko.readthedocs.io/ko/v0.4.3/install)
- sklearn
