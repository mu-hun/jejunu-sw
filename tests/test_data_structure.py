import sys
sys.path.append('Data Structure/handson/BinaryTree')
from stack import TreeStack
from stack import Node

def test_tree(capsys):
	n1 = Node('A')
	n2 = Node('B')
	n3 = Node('C')
	n4 = Node('D')
	n5 = Node('E')
	n6 = Node('F')
	n7 = Node('G')
	n8 = Node('H')

	n1.left = n2
	n1.right = n3
	n2.left = n4
	n2.right = n5
	n3.left = n6
	n3.right = n7
	n4.left = n8

	t = TreeStack(n1)
	t.preorder()
	assert capsys.readouterr().out == 'A B D H E C F G \n'
	t.inorder()
	assert capsys.readouterr().out == 'H D B E A F C G \n'
	t.stack_inorder()
	assert capsys.readouterr().out == 'H D B E A F C G \n'
	t.postorder()
	assert capsys.readouterr().out == 'H D E B F G C A \n'
	t.levelorder()
	assert capsys.readouterr().out == 'A B C D E F G H '
