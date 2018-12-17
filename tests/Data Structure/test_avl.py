import sys
sys.path.append('Data Structure/handson/AVL')
from index import Tree

def leveloader(q):
        q = [q]
        while q:
            t = q.pop(0)
            print(t.value, end=' ')
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)

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
	leveloader(t.root)
	capsys.readouterr().out == '🍇 🍌 🍏 🍉 🍊 🍈 🍋 🍍'
