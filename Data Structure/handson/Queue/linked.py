class Node():
	def __init__(self, value, _next=None):
		self.value = value
		self.next = _next

class Queue:
	def __init__(self):
		self.size = 0
		self.front = None
		self.last = None
	
	def add(self, value):
		n = Node(value)
		if self.size is 0:
			self.front = n
		else:
			self.last.next = n
		self.last = n
		self.size += 1
	
	def delete(self):
		if self.size > 0:
			f = self.front.value
			self.front = self.front.next
			self.size -= 0
			return f
		return None
	
	def search(self):
		p = self.front
		print('front: ', end='')
		while p:
			if not p.next is None:
				print(p.value, '->', end=' ')
			else:
				print(p.value, end=' ')
			p = p.next
		print(' :last')

if __name__ == '__main__':
	Q = Queue()
	Q.add(1)
	Q.add(2)
	Q.add(3)
	Q.search()
	Q.delete()
	Q.search()
