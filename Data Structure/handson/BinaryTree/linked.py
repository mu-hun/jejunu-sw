class Node():
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

class Tree():
	def __init__(self, n=None):
		self.root = n
		self.index = self.root

	def preorder(self, n):
		if n:
			print(str(n.value), ' ', end='')
		else:
			return
		if n.left:
			self.preorder(n.left)
		if n.right:
			self.preorder(n.right)
	
	def inorder(self, n):
		if n is None:
			return
		if n.left:
			self.preorder(n.left)
		print(str(n.value), ' ', end='')
		if n.right:
			self.preorder(n.right)
	
	def postorder(self, n):
		if n is None:
			return
		if n.left:
			self.preorder(n.left)
		if n.right:
			self.preorder(n.right)
		print(str(n.value), ' ', end='')
	
	def levelorder(self, root):
		q = []
		q.append(root)
		while len(q) > 0:
			t = q.pop(0)
			print(str(t.value), ' ', end='')
			if t.left:
				q.append(t.left)
			if t.right:
				q.append(t.right)
	
	def getHeight(self, root):
		return 0 if root is None else max(self.getHeight(root.left), self.getHeight(root.right)) + 1
	
	def copy_tree(self, n):
		pass

if __name__ == '__main__':
	t = Tree()
	n1 = Node('A')
	n2 = Node('B')
	n3 = Node('C')
	n4 = Node('D')
	n5 = Node('E')
	n6 = Node('F')
	n7 = Node('G')
	n8 = Node('H')
	
	# TODO: Tree append 구현
	
	n1.left = n2
	n1.right = n3

	# n2.left = n4
	# n2.right = n5
	# n3.left = n6
	# n3.right = n7
	# n4.left = n8

	n1.left.left = n4
	n1.left.right = n5

	n1.right.left = n6
	n1.right.right = n7

	n1.left.left.left = n8
	
	print('전위순회: ', end='')
	t.preorder(n1)
	print('\n중위순회: ', end='')
	t.inorder(n1)
	print('\n후위순회: ', end='')
	t.postorder(n1)
	print('\n레벨순회: ', end='')
	t.levelorder(n1)
	print('\n트리높이: ', end='')
	print(t.getHeight(n1))
