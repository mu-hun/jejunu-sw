def createSet():
    return [5, 0]


def isEmpty(s: list):
    return bool(s[1])


def cardinality(s: list):
    return s[1]


def isElement(x: int, a: list):
    return a[2:].count(x)


def addElement(x: int, a: list):
    if isElement(x, a):
        return False
    if cardinality(a) is a[0]:
        a[0] *= 2
    a.append(x)
    a[1] += 1
    a = a[:2] + sorted(a[2:])
    return a


def removeElement(x: int, a: list):
    if isElement(x, a):
        a.remove(x)
        a[1] -= 1
        return a
    return False


def isSubset(a: list, b: list):
    for i in a[2:]:
        if isElement(i, b):
            return True
    return False


def isEqual(a: list, b: list):
    return a[2:] == b[2:]


def isDisjoint(a: list, b: list):
    return not isSubset(a, b)


def intersection(a: list, b: list):
    result = createSet()
    for i in a[2:]:
        if isElement(i, b):
            result = addElement(i, result)
    return result


def union(a: list, b: list):
    result = createSet()
    while cardinality(a) and cardinality(b):
        if a[2] < b[2]:
            if not isElement(a[2], result):
                result = addElement(a[2], result)
            a = removeElement(a[2], a)
        else:
            if not isElement(b[2], result):
                result = addElement(b[2], result)
            b = removeElement(b[2], b)
    while cardinality(a):
        if not isElement(a[2], result):
                result = addElement(a[2], result)
        a = removeElement(a[2], a)
    while cardinality(b):
        if not isElement(b[2], result):
            result = addElement(b[2], result)
        b = removeElement(b[2], b)
    return result


def difference(a: list, b: list):
    result = createSet()
    inter = intersection(a, b)
    uni = union(a, b)
    for i in uni[2:]:
        if not isElement(i, inter):
            result = addElement(i, result)
    return result


def test_main():
    l = createSet()
    assert l == [5, 0]
    l = addElement(3, l)
    assert l == [5, 1, 3]
    m = createSet()
    m = addElement(2, addElement(7, addElement(4, m)))
    assert m == [5, 3, 2, 4, 7]
    assert union(l, m) == [5, 4, 2, 3, 4, 7]
    assert difference([5, 3, 1, 3, 4], [5, 2, 1, 4]) == [5, 1, 3]


if __name__ == '__main__':
    test_main()
