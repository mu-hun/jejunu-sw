def select_sort(_l):
	_len = len(_l)
	for i in range(_len):
		min = i
		for j in range(i, _len):
			if _l[min] > _l[j]:
				min = j
		_l[i], _l[min] = _l[min], _l[i]
	return _l


def insert_sort(_l):
	for i in range(1, len(_l)):
		x = _l[i]
		j = i - 1
		while j >= 0 and _l[j] > x:
			_l[j+1] = _l[j]
			j = j - 1
		_l[j+1] = x
	return _l


def shell_sort(_l):
	h = 4
	while h > 0:
		for i in range(h, len(_l)):
			j = i
			while j >= h and _l[j] < _l[j-h]:
				_l[j], _l[j-h] = _l[j-h], _l[j]
				j = j - h
		h = h // 3
	return _l


if __name__ == '__main__':
	l = [3, 4, 1]
	assert select_sort(l) == insert_sort(l) == shell_sort(l) == sorted(l)
