from node import Node

class EmptyError(Exception):
	pass

class List():
	def __init__(self):
		self.head = None
		self.size = 0
	
	def is_empty(self):
		return self.size == 0
	
	def delete_is_possible(self):
		if self.is_empty():
			raise EmptyError('Underflow')
	
	def insert_front(self, value):
		if self.is_empty():
			self.head = Node(value, None)
		else:
			self.head = Node(value, self.head)
		self.size += 1
	
	def insert_after(self, value, p):
		p.next = Node(value, p.next)
		self.size += 1
	
	def delete_front(self):
		self.delete_is_possible()
		self.head = self.head.next
		self.size += 1
	
	def delete_after(self, p):
		self.delete_is_possible()
		t = p.next
		if t is None:
			return
		else:
			p.next = t.next

	def search(self, value):
		t, index = self.head, 1
		while not (t.next is None):
			if t.value == value:
				return index
			else:
				t = t.next
				index = index + 1
		return None
	
	def print_list(self): # 연결리스트 출력
		p = self.head
		while p:
			if not p.next == None:
				print(p.value, ' -> ', end='')
			else:
				print(p.value)
			p = p.next

if __name__ == '__main__':
	s = List()

	s.insert_front('orange')
	s.insert_front('apple')
	s.insert_front('pear')
	s.insert_after('cherry', s.head) 

	s.print_list()

	print('cherry는  %d번째' % s.search('cherry'))
	print('kiwi는', s.search('kiwi'))

	print('배 다음 노드 삭제 후:\t\t', end='')
	s.delete_after(s.head)
	s.print_list()

	print('첫 노드 삭제 후:\t\t', end='')
	s.delete_front()
	s.print_list()
	
	print('첫 노드로 망고,딸기 삽입 후:\t', end='')
	s.insert_front('mango')
	s.insert_front('strawberry')
	s.print_list()
	
	print('사과 다음 노드 삭제 후:\t', end='')
	s.delete_after(s.head.next.next)
	s.print_list()
