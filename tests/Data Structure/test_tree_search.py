import sys
sys.path.append('Data Structure/handson/BinarySearch/')
from index import Tree

def test_main():
	t = Tree()
	t.put(10, '10')
	t.put(20, '20')
	t.put(30, '30')
	t.put(40, '40')
	t.put(50, '50')
	t.put(60, '60')
	t.put(70, '70')
	# TODO Fix: 'Tree' object has no attribute
	# assert t.min().key == 10
	# t.delete_min()
	# assert t.min().key == 20
	# t.delete(40)
	# assert t.getHeight() == 5
