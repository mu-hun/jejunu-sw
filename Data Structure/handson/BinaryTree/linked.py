class Node():
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

class Tree():

	def preorder(self, n):
		if n != None:
			print(n.value, end=' ')
			if n.left:
				self.preorder(n.left)
			if n.right:
				self.preorder(n.right)
	
	def inorder(self, n):
		if n != None:
			if n.left:
				self.inorder(n.left)
			print(n.value, end=' ')
			if n.right:
				self.inorder(n.right)
	
	def postorder(self, n):
		if n != None:
			if n.left:
				self.postorder(n.left)
			if n.right:
				self.postorder(n.right)
			print(n.value, end=' ')
	
	def levelorder(self, q):
		q = [q]
		while q:
			t = q.pop(0)
			print(t.value, end=' ')
			if t.left:
				q.append(t.left)
			if t.right:
				q.append(t.right)
	
	def getHeight(self, root):
		return 0 if root is None else max(self.getHeight(root.left), self.getHeight(root.right)) + 1
	
	def copy_tree(self, n):
		pass

if __name__ == '__main__':
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
	n2.left = n4
	n2.right = n5
	n3.left = n6
	n3.right = n7
	n4.left = n8

	t = Tree()
	
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
