from konlpy.tag import Mecab
from sklearn.feature_extraction.text import CountVectorizer


def getNVM(text: str):
    tokenizer = Mecab()
    parsed = tokenizer.pos(text)
    pos = []
    tags = ['NNG', 'NNP']
    for word in parsed:
        tag = word[1]
        if tag in tags:
            pos.append(word[0])
    return pos


def counter(words: tuple[str]):
    vector = CountVectorizer(
        tokenizer=getNVM, preprocessor=None, lowercase=None)
    DTM = vector.fit_transform(words)

    mapped = {}
    for index, _words in enumerate(vector.get_feature_names()):
        mapped[_words] = DTM.getcol(index).sum()

    return sorted(mapped.items(), key=lambda x: x[1], reverse=True)
