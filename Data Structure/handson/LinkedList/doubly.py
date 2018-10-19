class Node():
	def __init__(self, value, prev, _next):
		self.value = value
		self.prev = prev
		self.next = _next

class List():
	def __init__(self):
		self.head = Node(None, None, None)
		self.tail = Node(None, self.head, None)
		self.head.next = self.tail
		self.size = 0
	
	def is_empty(self):
		return self.size is 0
	
	def insert_prev(self, value, p):
		t = p.prev
		n = Node(value, t, p)
		t.next = n
		p.prev = n
		self.size = self.size + 1
	
	def insert_above(self, value, p):
		t = p.next
		n = Node(value, p, t)
		p.next = n
		t.prev = n
		self.size = self.size + 1
	
	def delete(self, x):
		p = x.prev
		a = x.next
		p.next = a
		a.prev = p
		self.size = self.size - 1
		return x.value
	
	def search(self):
		if self.is_empty():
			print('List is Empty')
		else:
			p = self.head.next
			while not p is self.tail:
				if not p.next is self.tail:
					print(p.value + ' <=> ', end='')
				else:
					print(p.value)
				p = p.next

if __name__ == '__main__':
    s = List()
    s.insert_above('apple', s.head)
    s.insert_prev('orange', s.tail)
    s.insert_prev('cherry', s.tail)
    s.insert_above('pear', s.head.next)
    s.search()
    print('마지막 노드 삭제 후:\t', end='')
    s.delete(s.tail.prev)
    s.search() 
    print('맨 끝에 포도 삽입 후:\t', end='')
    s.insert_prev('grape', s.tail)
    s.search()
    print('첫 노드 삭제 후:\t', end='')   
    s.delete(s.head.next)
    s.search()
    print('첫 노드 삭제 후:\t', end='')    
    s.delete(s.head.next)
    s.search()
    print('첫 노드 삭제 후:\t', end='') 
    s.delete(s.head.next)
    s.search()
    print('첫 노드 삭제 후:\t', end='') 
    s.delete(s.head.next)
    s.search()
