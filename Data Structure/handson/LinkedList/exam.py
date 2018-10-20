from node import Node
from simple import List

class EList(List):
	def split_list(self, k):
		p = self.head
		small, bigger = EList(), EList()
		while p:
			if not p == None:
				if p.value <= k:
					small.insert_front(p.value)
				else:
					bigger.insert_front(p.value)
			p = p.next
		return small, bigger

if __name__ == '__main__':
	s = EList()

	s.insert_front(2)
	s.insert_front(3)
	s.insert_front(3)
	s.insert_front(4)

	s.print_list()

	small, big = s.split_list(3)
	small.print_list()
	big.print_list()
