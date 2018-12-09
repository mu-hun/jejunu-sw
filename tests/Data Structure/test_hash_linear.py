import sys
sys.path.append('Data Structure/handson/Hash')
from Linear import LinearProbing

def test_main(capsys):
	t = LinearProbing(13)
	t.put(25, 'grape')
	t.put(37, 'apple')
	t.put(18, 'banana')
	t.put(55, 55)
	t.put(22, 22)
	t.put(35, 35)
	t.put(50, 50)
	t.put(63, 63)
	t.print_table()
	output = capsys.readouterr()
	assert output.out == '''0    1    2    3    4    5    6    7    8    9    10   11   12   
50   63   None 55   None 18   None None None 22   35   37   25   '''
