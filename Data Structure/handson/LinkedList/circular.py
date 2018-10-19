from node import Node
from doubly import List
from simple import EmptyError

class CList(List):
	def __init__(self):
		self.last = None
		self.size = 0
	
	def insert(self, value):
		n = Node(value, None)
		if self.is_empty():
			n.next = n
			self.last = n
		else:
			n.next = self.last.next
			self.last.next = n
		self.size = self.size + 1
	
	def delete(self):
		x = self.last.next
		if self.size is 0:
			self.last = None
		else:
			self.last.next = x.next
		self.size = self.size - 1
		return x.value
	
	def first(self):
		if self.is_empty():
			raise EmptyError('list is empty')
		f = self.last.next
		return f.value
	
	def search(self):
		if self.is_empty():
			print('list is empty')
		else:
			f = self.last.next
			p = f
			while not p.next is f:
				print(p.value + ' -> ', end='')
				p = p.next
			print(p.value)

if __name__ == '__main__':
    s = CList()
    s.insert('pear')
    s.insert('cherry')
    s.insert('orange')
    s.insert('apple') 
    s.search()
    print('s의 길이 =', s.size) 
    print('s의 첫 항목 :', s.first())
    s.delete() 
    print('첫 노드 삭제 후: ', end='')
    s.search()
    print('s의 길이 =', s.size) 
    print('s의 첫 항목 :', s.first()) 
    s.delete() 
    print('첫 노드 삭제 후: ', end='')
    s.search()
    s.delete() 
    print('첫 노드 삭제 후: ', end='')
    s.search()
    s.delete() 
    print('첫 노드 삭제 후: ', end='')
    s.search()
