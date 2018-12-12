from Linear import LinearProbing

class Node:
	def __init__(self, key, data, link):
		self.key = key
		self.data = data
		self.next = link

class Chaining(LinearProbing):
	def put(self, key, data):
		i = self.hash(key)
		p = self.a[i]
		while p:
			if key == p.key:
				p.data = data
				return
			p = p.next
		self.a[i] = Node(key, data, self.a[i])

	
	def get(self, key):
		i = self.hash(key)
		p = self.a[i]
		while p:
			if key == p.key:
				return p.data
			p = p.next
		return None
	
	def print_table(self):
		for i in range(self.M):
			print(i, end=' ')
			p = self.a[i]
			while p:
				print(f'-> [{p.key}, {p.data}]', end=' ')
				p = p.next

if __name__ == '__main__':
	t = Chaining(13)
	t.put(25, '🍇')
	t.put(37, '🍏')
	t.put(18, '🍌')
	t.put(55, '🍈')
	t.put(22, '🍉')
	t.put(35, '🍊')
	t.put(50, '🍋')
	t.put(63, '🍍')
	t.print_table()
