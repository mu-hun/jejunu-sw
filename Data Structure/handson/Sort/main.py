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

if __name__ == '__main__':
	print(select_sort([3, 4, 1]))
	print(insert_sort([3, 4, 1]))
