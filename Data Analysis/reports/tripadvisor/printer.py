from itertools import chain

import pandas as pd
from matplotlib import pyplot as plt, rc

from tokenizer import counter

if __name__ == "__main__":
    df = pd.read_csv('output.csv')
    reviews = tuple(chain.from_iterable(
        df.loc[:, ['제목', '본문']].values.tolist()))

    split_end_index = 20
    split_range = range(20)

    words = counter(reviews)[:split_end_index]

    rc('font', family='SpoqaHanSans')
    plt.rcParams['axes.unicode_minus'] = False

    plt.bar(split_range, tuple(map(lambda word: word[1], words)))
    plt.title('상위 20개 단어')
    plt.ylabel('빈도수')

    ax = plt.subplot()
    ax.set_xticks(split_range)
    ax.set_xticklabels(
        tuple(map(lambda word: word[0], words)), rotation=30)
    plt.show()
