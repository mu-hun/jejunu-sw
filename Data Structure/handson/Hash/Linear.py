class LinearProbing:
	def __init__(self, size):
		self.M = size
		self.a = [None for __ in range(size)]
		self.d = self.a.copy()

	def hash(self, key):
		return key % self.M

	def put(self, key, data):
		init_postion = self.hash(key)
		i = init_postion
		j = 0
		while True:
			if self.a[i] is None:
				self.a[i] = key
				self.d[i] = data
				return
			if self.a[i] == key:
				self.d[i] = data
				return
			j = j + 1
			i = (init_postion + j) % self.M  # 11 % 11 = 0
			if i == init_postion:
				break  # 초기 위치라면 저장 실패

	def get(self, key):
		init_postion = self.hash(key)
		i = init_postion
		j = 1
		while self.a[i]:
			if self.a[i] == key:
				return self.d[i]
			i = (init_postion + j) % self.M
			j = j + 1
			if i == init_postion:
				return None
		return None

	def print_table(self):
		for i in range(self.M):
			print('{:4}'.format(str(i)), end=' ')
		print()
		for i in range(self.M):
			print('{:4}'.format(str(self.a[i])), end=' ')


if __name__ == '__main__':
	t = LinearProbing(13)
	t.put(25, 'grape')
	t.put(37, 'apple')
	t.put(18, 'banana')
	t.put(55, 55)
	t.put(22, 22)
	t.put(35, 35)
	t.put(50, 50)
	t.put(63, 63)
	t.print_table()
