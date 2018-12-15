from AVL.main import Tree

def test_main(capsys):
	t = Tree()
	t.put(25, '🍇')
	t.put(37, '🍏')
	t.put(18, '🍌')
	t.put(55, '🍈')
	t.put(22, '🍉')
	t.put(35, '🍊')
	t.put(50, '🍋')
	t.put(63, '🍍')
	t.levelorder(t.root)
	capsys.readouterr().out == '🍇 🍌 🍏 🍉 🍊 🍈 🍋 🍍'
