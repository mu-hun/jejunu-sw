class Stack:
	def __init__(self):
		self.elements = []
	 
	def push(self, value):
		self.elements.append(value)
	
	def pop(self):
		if self.is_empty():
			return None
		self.elements.pop()
	
	def size(self):
		return len(self.elements)

	def is_empty(self):
		return self.size() is 0
