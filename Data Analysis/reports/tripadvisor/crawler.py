import pandas as pd

from graphql import run_query

endpoint = 'https://www.tripadvisor.co.kr/data/graphql'

query = """
query ReviewList(
  $locationId: Int!
  $offset: Int
  $limit: Int
  $filters: [FilterConditionInput!]
  $prefs: ReviewListPrefsInput
  $initialPrefs: ReviewListPrefsInput
  $filterCacheKey: String
  $prefsCacheKey: String
) {
  locations(locationIds: [$locationId]) {
    reviewListPage(
      page: { offset: $offset, limit: $limit }
      filters: $filters
      prefs: $prefs
      initialPrefs: $initialPrefs
      filterCacheKey: $filterCacheKey
      prefsCacheKey: $prefsCacheKey
    ) {
      reviews {
        ... on Review {
          publishedDate
          title
          text
          rating
        }
      }
    }
  }
}
"""

header = ['발행 날짜', '제목', '본문', '평가']
keys = {'발행 날짜': 'publishedDate',
        '제목': 'title', '본문': 'text', '평가': 'rating'}


def initial_variables(offset: int):
    return {
        "filterCacheKey": "locationReviewFilters_550726",
        "filters": [{"axis": "LANGUAGE", "selections": ["ko"]}],
        "initialPrefs": {},
        "keywordVariant": "location_keywords_v2_llr_order_30_ko",
        "limit": 20,
        "locationId": 550726,
        "needKeywords": False,
        "offset": offset,
        "prefs": None,
        "prefsCacheKey": "locationReviewPrefs"
    }


if __name__ == "__main__":
    total_count = 1072
    offset = 0

    reviews = []

    while offset < total_count:
        data = run_query(endpoint, query, initial_variables(offset))[
            'data']['locations'][0]['reviewListPage']['reviews']
        reviews += data
        offset += 20

    def mapper(review):
        return list(map(lambda key: review[keys[key]], header))

    pd.DataFrame(list(map(mapper, reviews))).to_csv(
        'output.csv', header=header, index=None)
