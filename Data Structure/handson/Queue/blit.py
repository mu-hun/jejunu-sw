class Queue:
	def __init__(self):
		self.list = []
	
	def add(self, value):
		self.list.append(value)
	
	def delete(self):
		if len(self.list) > 0:
			return self.list.pop(0)
	
	def search(self):
		print('front ->', end=' ')
		for i in self.list:
			print(i, '<-', end=' ')
		print('last')

if __name__ == '__main__':
	Q = Queue()
	Q.add(1)
	Q.add(2)
	Q.search()
