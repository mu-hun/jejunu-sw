from math import sqrt
from operator import itemgetter
from functools import reduce

sinfo = [
    [100, 85, 90, 87],
    [101, 90, 83, 90],
    [102, 83, 90, 79],
    [103, 91, 78, 80],
    [104, 84, 90, 90],
    [105, 94, 85, 77],
    [107, 82, 90, 88],
    [108, 98, 90, 90],
    [109, 81, 81, 85],
    [110, 78, 90, 90]
]


def calculateGrade(L: list):
    return reduce(lambda x, y: x + y, [L[i]/v for i, v in enumerate([5, 2.5, 2.5])])


snumber = list(map(calculateGrade, sinfo))

new_sinfo = [[v[0], snumber[i]] for i, v in enumerate(sinfo)]

for i, v in enumerate(sorted(new_sinfo, key=itemgetter(1), reverse=True)[:11]):
    print(f'{i+1}등: 학번 {v[0]}, 점수: {v[1]}')

# 2 - 1

mybooks = [
    {"제목": "안드로이드앱개발", "저자": "최전산", "출판사": "PCBOOK", "가격": 25000, "출판년도": 2010},
    {"제목": "영재교육의원리", "저자": "김정희", "출판사": "생능출판사", "가격": 22000, "출판년도": 2011},
    {"제목": "파이썬", "저자": "강수라", "출판사": "이한출판사", "가격": 23000, "출판년도": 2010},
    {"제목": "중독상담과재활", "저자": "유지희", "출판사": "정익사", "가격": 35000, "출판년도": 2012},
    {"제목": "협동학습", "저자": "이유리", "출판사": "이한출판사", "가격": 30000, "출판년도": 2013},
    {"제목": "자바스크립트", "저자": "박정식", "출판사": "SAMS", "가격": 38000, "출판년도": 2014},
    {"제목": "HTML5", "저자": "주환", "출판사": "생능출판사", "가격": 33000, "출판년도": 2012},
    {"제목": "컴파일러", "저자": "장진웅", "출판사": "PCBOOK", "가격": 24000, "출판년도": 2011},
    {"제목": "C언어", "저자": "홍말숙", "출판사": "한빛미디어", "가격": 29000, "출판년도": 2010},
    {"제목": "프로그래밍비타민", "저자": "현정숙", "출판사": "정익사", "가격": 41000, "출판년도": 2009},
    {"제목": "안드로이드", "저자": "이광희", "출판사": "한빛미디어", "가격": 42000, "출판년도": 2013},
    {"제목": "앱인벤터", "저자": "박규진", "출판사": "생능출판사", "가격": 30000, "출판년도": 2015}]


def selectYear(year: int):
    for i in filter(lambda x: x["출판년도"] == year, mybooks):
        print(f'''
		제목 : {i['제목']}
		저자: {i['저자']}''')


selectYear(int(input('찾는 책의 출판 년도를 입력해주세요: ')))

# 2 - 2


def makeTitle(L: list):
    _L = []
    for i, v in enumerate(L):
        _L.append(f"{i+1}. {v['제목']}")
    return reduce(lambda x, y: f"{x}\n{y}", _L)


_input = int(input(f"다음 도서 중 하나를 선택하세요.\n{makeTitle(mybooks)} \n번호는? ")) - 1
for k in mybooks[_input].keys():
    print(f"* {k}: {mybooks[_input][k]}")

# 3

# filter, map enumerate, [Dict 혹은 array].keys(), sorted() 등 1 ~ 2 답안에 이미 사용함

# 4


def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

# 함수형 버전

def distance2(x1, y1):
    return lambda x2, y2: sqrt((x1-x2)**2 + (y1-y2)**2)


# 사용 케이스 1
distance2(0, 0)(1, 1)

# 사용케이스 2
fixed = distance2(0, 0)
fixed(1, 1)

# 5


def isleapyear(y):
    return not(y % 4) and not(y % 100) or not(y % 400)
