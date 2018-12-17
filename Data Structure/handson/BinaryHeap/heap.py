class Heap:
	def __init__(self, _list):
		self.list = _list
	
	def min_create(self):
		for i in range(self.getSize()//2, 0, -1):
			self.downHeap(i)
	
	def insert(self, kv):
		self.list.append(kv)
		self.upHeap(self.getSize())
	
	def delete_min(self):
		if self.getSize() is 0:
			print("heap is Empty")
			return None
		min = self.list[1]
		self.list[1], self.list[-1] = self.list[-1], self.list[1]
		del self.list[-1]
		self.downHeap()
		return min
	
	def downHeap(self, i=1):
		while 2*i <= self.getSize():
			k = 2*i
			if k < self.getSize() and self.list[k][0] > self.list[k+1][0]:
				k += 1
			if self.list[i][0] < self.list[k][0]:
				break 
			self.list[i], self.list[k] = self.list[k], self.list[i]
			i = k
	
	def upHeap(self, j):
		while j > 1 and self.list[j//2][0] > self.list[j][0]:
			self.list[j], self.list[j//2] = self.list[j//2], self.list[j]
			j = j//2
	
	def print_heap(self):
		for i in self.list[1:]:
			print(f'[{i[0]}, {i[1]}]', end='')
	
	def getSize(self):
		return len(self.list) - 1


if __name__ == '__main__':
	a = [None, [90, 'watermelon'], [80, 'pear'], [70, 'melon'], [50, 'lime'], [60, 'mango'], [20, 'cherry'], [30, 'grape'], [35, 'orange'], [10, 'apricot'], [15, 'banana'], [45, 'lemon'], [40, 'kiwi']]
	
	b = Heap(a)
	
	print('힙 만들기 전:', end=' ')
	b.print_heap()
	print(f'\n크기: {b.getSize()}')

	print('최소힙:', end=' ')
	b.min_create() # O(n)
	b.print_heap()
	print(f'\n크기: {b.getSize()}')

	print('최솟값 삭제 후:', end=' ')
	b.delete_min()
	b.print_heap()
	print(f'\n크기: {b.getSize()}')

	print('5 삽입 후')
	b.insert([5,'apple']) # O(log n)
	b.print_heap()
	print(f'\n크기: {b.getSize()}')
5
