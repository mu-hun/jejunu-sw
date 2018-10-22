class Node():
	def __init__(self, value, _next=None):
		self.value = value
		self.next = _next

class Stack:
	def __init__(self):
		self.top = None
		self.size = 0
		
	def push(self, value):
		self.top = Node(value, self.top)
		self.size += 1
	
	def pop(self):
		if self.size > 0:
			top_value = self.top.value
			self.top = self.top.next
			self.size -= 1
			return top_value

	def peek(self):
		if self.size > 0:
			return self.top.value
	
	def search(self):
		print('top -> \t', end='')
		p = self.top
		while p:
			if not p.next is None:
				print(p.value, '-> ', end='')
			else:
				print(p.value, end='')
			p = p.next

if __name__ == '__main__':
	s = Stack()
	s.push(1)
	print(s.peek())
	s.push(3)
	s.pop()
	s.push(2)
	s.search()
