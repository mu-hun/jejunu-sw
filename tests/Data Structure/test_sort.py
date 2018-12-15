import sys
sys.path.append('Data Structure/handson/Sort')

from main import *

def test_main():
	l = [3, 4, 1]
	assert select_sort(l) == insert_sort(l) == shell_sort(l) == sorted(l)
