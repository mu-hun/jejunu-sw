import sys
sys.path.append('Data Structure/handson/BinaryTree')
from stack import TreeStack
from linked import Node
from linked import Tree


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
    tr = Tree()

    t.preorder()
    t_read = capsys.readouterr()
    tr.preorder(n1)
    tr_read = capsys.readouterr()
    assert t_read.out == tr_read.out

    t.inorder()
    t_read = capsys.readouterr()
    tr.inorder(n1)
    tr_read = capsys.readouterr()
    assert t_read.out == tr_read.out

    t.inorder_without_stack()
    t_read = capsys.readouterr()
    tr.inorder(n1)
    tr_read = capsys.readouterr()
    assert t_read.out == tr_read.out

    t.postorder()
    t_read = capsys.readouterr()
    tr.postorder(n1)
    tr_read = capsys.readouterr()
    assert t_read.out == tr_read.out

# def test_heap():
