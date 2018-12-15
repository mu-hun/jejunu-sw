import sys
sys.path.append('Data Structure/handson/Sort')

from main import select_sort, insert_sort

def test_main():
	assert select_sort([3, 4, 1]) == insert_sort([3, 4, 1]) == [1, 3, 4]
