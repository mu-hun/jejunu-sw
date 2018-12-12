import sys
sys.path.append('Data Structure/handson/Hash')
from Chain import Chaining

def test_main(capsys):
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
	output = capsys.readouterr()
	assert output.out == '0 1 2 3 -> [55, 🍈] 4 5 -> [18, 🍌] 6 7 8 9 -> [35, 🍊] -> [22, 🍉] 10 11 -> [63, 🍍] -> [50, 🍋] -> [37, 🍏] 12 -> [25, 🍇] '
